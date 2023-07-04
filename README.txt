NPR Sentiment Analysis Program

This program performs sentiment analysis on articles from the National Public Radio (NPR) website. It extracts the content of the article from the provided URL, analyzes its sentiment using the VADER sentiment analysis tool, and displays the results indicating whether the sentiment is positive or negative.

Requirements:
- Python 3.x
- newspaper3k library
- nltk library

Installation:
1. Install Python 3.x from the official Python website: https://www.python.org/downloads/
2. Install the required libraries by running the following command in the terminal:
   pip install newspaper3k nltk

Usage:
1. Run the program by executing the Python script: `python npr_sentiment_analysis.py`.
2. Enter the URL of an NPR article in the provided URL entry field.
3. Click the "Analyze" button to perform sentiment analysis on the article.
4. The results, including the article title, URL, and sentiment label, will be displayed in the output text field.
5. You can scroll through the output text field using the scrollbar.
6. To clear the results, click the "Clear" button.

Note: Internet connectivity is required to download and analyze the articles.

Credits:
- This program utilizes the newspaper3k library for article extraction.
- Sentiment analysis is performed using the VADER (Valence Aware Dictionary and sEntiment Reasoner) sentiment analysis tool from the nltk library.





License:
This project is licensed under the [insert license name]. Please see the LICENSE file for more details.
