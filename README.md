# Data Extraction and NLP Analysis

## Project Overview

This project involves extracting article text from given URLs and performing text analysis to compute various metrics. The aim is to analyze sentiment and readability of the articles and generate structured output based on predefined variables.
### Project Significance

This project is vital for extracting and analyzing text from online articles. It offers insights into:

1. **Sentiment Analysis:** Helps understand public opinion and improve customer experiences by evaluating the emotional tone of content.
   
2. **Readability Analysis:** Assesses how easily content can be understood, aiding in creating clearer and more engaging materials.

These analyses are essential for tailoring strategies, enhancing communication, and optimizing content quality in various fields.


## Table of Contents

1.  [Project Overview](#project-overview)
2.  [Project Significance](#project-significance)
3.  [Objective](#objective)
4.  [Installation](#installation)
5.  [File Structure](#file-structure)
6.  [Data Extraction](#data-extraction)
7.  [Data Analysis](#data-analysis)
8.  [Output Variables](#output-variables)
9.  [Notes](#notes)
10.  [License](#license)

## Objective

The objective of this project is to:

1. Extract article text from specified URLs.
2. Perform textual analysis to compute metrics including sentiment scores, readability indices, and other text-related variables.
3. Save the results in a structured format.

## Installation

To set up this project on your local machine, follow these steps:

1. **Ensure you have Python installed (version 3.7 or higher):**

   - Download and install Python from the official [Python website](https://www.python.org/downloads/).

2. **Install the required Python libraries:**

   Open your terminal and run the following command to install the necessary libraries:

   ```bash
   pip install pandas beautifulsoup4 requests nltk openpyxl
   ```

## File Structure

-   `data_extraction_nlp.py`: The main Python script for data extraction and analysis.
-   `README.md`: This file containing project information and instructions.

## Data Extraction

1. **Extracting Article Text:**

   - The script extracts text from provided URLs, focusing solely on the article content (title and body) while excluding headers, footers, and other non-article elements.
   - Each article's text is saved in a separate file, named with a unique identifier.

2. **Libraries Used:**

   - `BeautifulSoup` for parsing HTML.
   - `Requests` for fetching web pages.

## Data Analysis

1. **Sentimental Analysis:**

   - **Positive Score:** Computed based on a dictionary of positive words.
   - **Negative Score:** Computed based on a dictionary of negative words.
   - **Polarity Score:** Calculated as `(Positive Score - Negative Score) / (Positive Score + Negative Score + 0.000001)`.
   - **Subjectivity Score:** Calculated as `(Positive Score + Negative Score) / (Total Words + 0.000001)`.

2. **Readability Analysis:**

   - **Average Sentence Length:** Number of words divided by the number of sentences.
   - **Percentage of Complex Words:** Number of complex words divided by the total number of words.
   - **Fog Index:** Calculated using `0.4 * (Average Sentence Length + Percentage of Complex Words)`.

3. **Additional Metrics:**

   - **AVG Number of Words Per Sentence**
   - **Complex Word Count**
   - **Word Count**
   - **Syllable Per Word**
   - **Personal Pronouns**
   - **AVG Word Length**

## Output Variables

The output will include the following variables for each article:

- **POSITIVE SCORE**
- **NEGATIVE SCORE**
- **POLARITY SCORE**
- **SUBJECTIVITY SCORE**
- **AVG SENTENCE LENGTH**
- **PERCENTAGE OF COMPLEX WORDS**
- **FOG INDEX**
- **AVG NUMBER OF WORDS PER SENTENCE**
- **COMPLEX WORD COUNT**
- **WORD COUNT**
- **SYLLABLE PER WORD**
- **PERSONAL PRONOUNS**
- **AVG WORD LENGTH**

## Notes

- Ensure all dependencies are installed as outlined in the [Installation](#installation) section.
- The text extraction relies on HTML parsing libraries and may need adjustments based on the website’s structure.
- For detailed analysis, refer to the script for calculations and methodologies.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.




```python

```
