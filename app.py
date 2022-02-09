from flask import Flask
from flask.logging import create_logger
import logging
import requests
#import nltk
#import nltkmodules
import regex as re
from bs4 import BeautifulSoup
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words


app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)


def getabstract(subject):
    """parameter"""
 
    url = 'https://en.wikipedia.org/w/api.php'
    params = {
            'action': 'parse',
            'page': subject,
            'format': 'json',
            'prop':'text',
            'redirects':''
            }
 
    response = requests.get(url, params=params)
    data = response.json()
 
    raw_html = data['parse']['text']['*']
    soup = BeautifulSoup(raw_html,'html.parser')
    soup.find_all('p')
    text = ''
 
    for p in soup.find_all('p'):
        text += p.text
    
    return text  


@app.route("/get_wiki_summary_methoda/<subject>")
def get_wiki_summary_a(subject):
    text = getabstract(subject)
    stemmer = Stemmer('english') #Stemmer
    Tsummarizer=TextRankSummarizer(stemmer)#Initializing the TextRank Summarizer Object with stemmer
    Tsummarizer.stop_words = get_stop_words('english') #Removing the stopwords
    parser = PlaintextParser.from_string(text, Tokenizer('english')) #Parsing the text
    summary=Tsummarizer(parser.document, 10) #Creating the TextRank based Summary
    final_answer=""
    for i in summary:
        final_answer=final_answer+str(i)
    final_answer=re.sub(r'[\d+]','', final_answer)
    return re.sub(r'\[\]','', final_answer)
  
@app.route("/get_wiki_summary_methodb/<subject>")
def get_wiki_summary_b(subject):
    text = getabstract(subject)
    stemmer = Stemmer('english') #Stemmer
    Lsummarizer=LexRankSummarizer(stemmer)#Initializing the TextRank Summarizer Object with stemmer
    Lsummarizer.stop_words = get_stop_words('english') #Removing the stopwords
    parser = PlaintextParser.from_string(text, Tokenizer('english')) #Parsing the text
    summary=Lsummarizer(parser.document, 10) #Creating the TextRank based Summary
    final_answer=""
    for i in summary:
        final_answer=final_answer+str(i)
    final_answer=re.sub(r'[\d+]','', final_answer)
    return re.sub(r'\[\]','', final_answer)  
  
@app.route("/")
def home():
    html = "<h3>Hi! Wikipedia Summary: Use get_wiki_summary_methoda/subject to get 10 sentences that summarize the abstract using TextRank and get_wiki_summary_methodb/subject to get 10 sentences that summarize the abstract using LexRank.</h3>"
    return html.format(format)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
