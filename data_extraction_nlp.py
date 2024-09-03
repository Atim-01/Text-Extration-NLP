#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd           
import requests                
from bs4 import BeautifulSoup  

# Read the Excel file
df = pd.read_excel(r'C:\Users\Administrator\Downloads\Copy of Input.xlsx') 


# In[ ]:


# Loop through each URL in the DataFrame
for index, row in df.iterrows():
    url_id = row['URL_ID']          # Extract the URL_ID from the current row
    url = row['URL']                # Extract the URL from the current row
    
    try:
        
        response = requests.get(url)
        response.raise_for_status() 
        
        html_content = response.content  
        
        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Extract the title of the article
        # Check for different variations in the HTML structure to find the title
        title_tag = soup.find('h1', class_='entry-title')  
        if not title_tag:
            title_tag = soup.find('h1', class_='tdb-title-text') 
        
        # Get the text of the title tag if it exists, otherwise set as 'No Title'
        title = title_tag.text.strip() if title_tag else 'No Title'
        
        # Extract the main content of the article
        # Check for different variations in the HTML structure to find the content
        content_tag = soup.find('div', class_='td-post-content tagdiv-type')  
        if not content_tag:
            content_tag = soup.find('div', class_='td_block_wrap tdb_single_content tdi_130 td-pb-border-top td_block_template_1 td-post-content tagdiv-type')  
        
        # Get the text of the content tag if it exists, otherwise set as 'No Content'
        content = content_tag.text.strip() if content_tag else 'No Content'
        
        # Write the title and content to a text file named with the URL_ID
        with open(f'{url_id}.txt', 'w', encoding='utf-8') as file:
            file.write(f"{title}\n\n")
            file.write(content)
    
    except requests.exceptions.RequestException as e:
        # Handle exceptions related to the HTTP request
        print(f"Failed to fetch {url}: {e}")
    except Exception as e:
        # Handle any other exceptions that may occur
        print(f"An error occurred for {url_id}: {e}")
        
# Print completion message
print("Scraping completed.")


# In[ ]:


import gdown
import os
import glob

# Define the URLs for your stop words and dictionary files
stop_words_urls = {
    'Copy of StopWords_Names.txt': 'https://drive.google.com/uc?export=download&id=1LLYnOnqRV1BPbmWYcSPx2Xox2-Smd42m', 
    'Copy of StopWords_Geographic.txt': 'https://drive.google.com/uc?export=download&id=1yp-sCMJUb5DU0ECTFx87JvPn-cpewrKF', 
    'Copy of StopWords_GenericLong.txt': 'https://drive.google.com/uc?export=download&id=11EYZSnP4Gdpyp9iNs1i98elC6-GOPevr',
    'Copy of StopWords_Generic.txt': 'https://drive.google.com/uc?export=download&id=1kOOlkQdBQbQXzLjTBceXXXB0C5eNDpnw',
    'Copy of StopWords_DatesandNumbers.txt': 'https://drive.google.com/uc?export=download&id=1dzFyfmXlhgeqC5GcSc4hOyOE8hUvZ2tp',
    'Copy of StopWords_Currencies.txt': 'https://drive.google.com/uc?export=download&id=1VwVEJ1iN-KPAlwIQIg9d5WgIgNeqrnJ4'
}

master_dictionary_urls = {
    'Copy of positive-words.txt': 'https://drive.google.com/uc?export=download&id=1EYSblvzrwKlo28hvjaF1lpOLdhlVyDvi',  
    'Copy of negative-words.txt': 'https://drive.google.com/uc?export=download&id=14_YmIixxmBTj1aXdPSJRU6mHKVCeygMO'   
}

# Define paths for storing the files
stopwords_path = 'stopwords'
master_dictionary_path = 'masterdictionary'

# Ensure the directories exist
os.makedirs(stopwords_path, exist_ok=True)
os.makedirs(master_dictionary_path, exist_ok=True)

# Download the stop words files
for filename, url in stop_words_urls.items():
    output = os.path.join(stopwords_path, filename)
    gdown.download(url, output, quiet=False)

# Download the master dictionary files
for filename, url in master_dictionary_urls.items():
    output = os.path.join(master_dictionary_path, filename)
    gdown.download(url, output, quiet=False)

# Verify the downloaded files
for path, urls in [(stopwords_path, stop_words_urls), (master_dictionary_path, master_dictionary_urls)]:
    for filename in urls.keys():
        file_path = os.path.join(path, filename)
        if os.path.exists(file_path):
            print(f'{file_path} exists.')
            with open(file_path, 'r', encoding='utf-8') as file:
                print(f'First few lines of {file_path}:')
                for _ in range(3):
                    print(file.readline().strip())
        else:
            print(f'{file_path} does not exist.')


# In[ ]:


import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import re
import os

# Load custom stop words from files in the specified directory
def load_stop_words(path):
    stop_words = set()
    for filename in os.listdir(path):
        with open(os.path.join(path, filename), 'r', encoding='latin-1') as file:
            stop_words.update(file.read().split())
    return stop_words

# Load a dictionary (e.g., positive or negative words) from a file
def load_dictionary(path):
    with open(path, 'r', encoding='latin-1') as file:
        return set(file.read().split())

# Clean text by tokenizing, removing non-alphanumeric words, converting to lowercase, and removing stop words
def clean_text(text, stop_words):
    words = word_tokenize(text)
    words = [word for word in words if word.isalnum()]
    words = [word.lower() for word in words if word.lower() not in stop_words]
    return words

# Calculate sentiment scores based on the presence of positive and negative words
def calculate_sentiment_scores(tokens, positive_words, negative_words):
    positive_score = sum(1 for word in tokens if word in positive_words)
    negative_score = sum(1 for word in tokens if word in negative_words)
    polarity_score = (positive_score - negative_score) / ((positive_score + negative_score) + 0.000001)
    subjectivity_score = (positive_score + negative_score) / (len(tokens) + 0.000001)
    return positive_score, negative_score, polarity_score, subjectivity_score

# Count the number of syllables in a word
def syllable_count(word):
    word = word.lower()
    syllables = re.findall(r'[aeiouy]+', word)
    return len(syllables)

# Calculate various readability metrics for the given text
def calculate_readability_metrics(text):
    sentences = sent_tokenize(text)
    words = word_tokenize(text)
    words = [word for word in words if word.isalnum()]
    
    num_words = len(words)
    num_sentences = len(sentences)
    avg_sentence_length = num_words / num_sentences if num_sentences > 0 else 0
    
    complex_words = [word for word in words if syllable_count(word) > 2]
    num_complex_words = len(complex_words)
    percentage_complex_words = num_complex_words / num_words if num_words > 0 else 0
    
    fog_index = 0.4 * (avg_sentence_length + percentage_complex_words)
    
    avg_words_per_sentence = num_words / num_sentences if num_sentences > 0 else 0
    
    syllables_per_word = sum(syllable_count(word) for word in words) / num_words if num_words > 0 else 0
    
    personal_pronouns = len(re.findall(r'\b(I|we|my|ours|us)\b', text, re.I))
    
    avg_word_length = sum(len(word) for word in words) / num_words if num_words > 0 else 0
    
    return avg_sentence_length, percentage_complex_words, fog_index, avg_words_per_sentence, num_complex_words, num_words, syllables_per_word, personal_pronouns, avg_word_length


# In[ ]:


import pandas as pd

# Read the Excel file
df = pd.read_excel(r'C:\Users\Administrator\Downloads\Copy of Input.xlsx') 

# Load stop words and dictionaries
stop_words = load_stop_words('stopwords')
positive_words = load_dictionary('masterdictionary/Copy of positive-words.txt')
negative_words = load_dictionary('masterdictionary/Copy of negative-words.txt')


# In[ ]:


# Initialize lists to store results
url_ids = []
urls = []
positive_scores = []
negative_scores = []
polarity_scores = []
subjectivity_scores = []
avg_sentence_lengths = []
percentage_complex_words = []
fog_indices = []
avg_words_per_sentence = []
complex_word_counts = []
word_counts = []
syllables_per_word = []
personal_pronouns = []
avg_word_lengths = []


# In[ ]:


# Loop through each URL
for index, row in df.iterrows():
    url_id = row['URL_ID']
    url = row['URL']
    
    try:
        with open(f'{url_id}.txt', 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Clean the text
        tokens = clean_text(content, stop_words)
        
        # Sentiment scores
        pos_score, neg_score, pol_score, subj_score = calculate_sentiment_scores(tokens, positive_words, negative_words)
        
        # Readability metrics
        avg_sent_len, perc_complex_words, fog_idx, avg_words_sent, complex_word_count, word_count, syll_per_word, personal_pronoun_count, avg_word_len = calculate_readability_metrics(content)
        
        # Append results to lists
        url_ids.append(url_id)
        urls.append(url)
        positive_scores.append(pos_score)
        negative_scores.append(neg_score)
        polarity_scores.append(pol_score)
        subjectivity_scores.append(subj_score)
        avg_sentence_lengths.append(avg_sent_len)
        percentage_complex_words.append(perc_complex_words)
        fog_indices.append(fog_idx)
        avg_words_per_sentence.append(avg_words_sent)
        complex_word_counts.append(complex_word_count)
        word_counts.append(word_count)
        syllables_per_word.append(syll_per_word)
        personal_pronouns.append(personal_pronoun_count)
        avg_word_lengths.append(avg_word_len)
        
        print(f"Successfully processed {url_id}")
    
    except Exception as e:
        print(f"An error occurred for {url_id}: {e}")


# In[ ]:


# Create a DataFrame with the results
results_df = pd.DataFrame({
    'URL_ID': url_ids,
    'URL': urls,
    'POSITIVE SCORE': positive_scores,
    'NEGATIVE SCORE': negative_scores,
    'POLARITY SCORE': polarity_scores,
    'SUBJECTIVITY SCORE': subjectivity_scores,
    'AVG SENTENCE LENGTH': avg_sentence_lengths,
    'PERCENTAGE OF COMPLEX WORDS': percentage_complex_words,
    'FOG INDEX': fog_indices,
    'AVG NUMBER OF WORDS PER SENTENCE': avg_words_per_sentence,
    'COMPLEX WORD COUNT': complex_word_counts,
    'WORD COUNT': word_counts,
    'SYLLABLE PER WORD': syllables_per_word,
    'PERSONAL PRONOUNS': personal_pronouns,
    'AVG WORD LENGTH': avg_word_lengths
})


# In[ ]:


# Save the results to a CSV file
results_df.to_csv('Output_Data.csv', index=False)


# In[ ]:


print("Analysis completed and results saved to Output_Data.csv")


# In[ ]:




