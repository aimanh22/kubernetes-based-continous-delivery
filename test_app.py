from app import getabstract
import requests
import regex as re
from bs4 import BeautifulSoup
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

def test_wiki():
   url = 'https://en.wikipedia.org/w/api.php'
   params = {
            'action': 'parse',
            'page': "Hello",
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
      pass
   stemmer = Stemmer('english') #Stemmer
   Tsummarizer=TextRankSummarizer(stemmer)#Initializing the TextRank Summarizer Object with stemmer
   Tsummarizer.stop_words = get_stop_words('english') #Removing the stopwords
   parser = PlaintextParser.from_string(text, Tokenizer('english')) #Parsing the text
   summary=Tsummarizer(parser.document, 10) #Creating the TextRank based Summary
   final_answer=""
   for i in summary:
      final_answer=final_answer+str(i)
   final_answer=re.sub(r'[\d+]','', final_answer)
   final_answer=re.sub(r'\[\]','', final_answer)
   
   assert get_wiki_summary_a("Hello")==final_answer
