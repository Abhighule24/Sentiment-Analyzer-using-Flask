from flask import Flask, request, render_template
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
from string import punctuation
import re
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('vader_lexicon')
set(stopwords.words('english'))
stop_words = stopwords.words('english')
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('home.html')

@app.route('/', methods =["POST"]) 
def AnalyseFunction():
    sentence = request.form.get("sent_text") 
    print(sentence)
    text2 = ''.join(c for c in sentence if not c.isdigit())
    text3 = ''.join(c for c in text2 if c not in punctuation) 
    processed_doc1 = ' '.join([word for word in text3.split(" ") if word not in stop_words])
    print(processed_doc1)
    sa = SentimentIntensityAnalyzer()
    score = sa.polarity_scores(text=text2)
    print(score)
    return render_template('home.html',text2=score['pos'],text3=score['neu'],text4=score['neg'],text5=score['compound'])

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5002, threaded=True)