import tkinter as tk
from newspaper import Article
from nltk.sentiment import SentimentIntensityAnalyzer

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

def analyze_sentiment(url):
    article = Article(url)
    article.download()
    article.parse()

    sentiment_scores = sia.polarity_scores(article.text)
    compound_score = sentiment_scores['compound']
    sentiment_label = "Positive" if compound_score >= 0 else "Negative"

    result = f"Title: {article.title}\nURL: {url}\nSentiment: {sentiment_label}\n\n"
    results_text.insert(tk.END, result)

def clear_results():
    results_text.delete("1.0", tk.END)

def on_analyze_click():
    url = url_entry.get()
    analyze_sentiment(url)
    url_entry.delete(0, tk.END)  # Clear the URL entry box

# Create a simple GUI using Tkinter
window = tk.Tk()
window.title("NPR Sentiment Analysis")

# Analyze button
analyze_button = tk.Button(window, text="Analyze", command=on_analyze_click)
analyze_button.pack()

# URL entry field
url_entry = tk.Entry(window, width=50)
url_entry.pack()

# Result text field with scrollbar
results_frame = tk.Frame(window)
results_frame.pack()

results_text = tk.Text(results_frame, height=20, width=80)
results_text.pack(side=tk.LEFT)

results_scrollbar = tk.Scrollbar(results_frame)
results_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configure scrollbar
results_text.config(yscrollcommand=results_scrollbar.set)
results_scrollbar.config(command=results_text.yview)

# Clear button
clear_button = tk.Button(window, text="Clear", command=clear_results)
clear_button.pack()

# Start the GUI event loop
window.mainloop()














