from nltk import tokenize
from nltk.corpus import stopwords
import nltk
import re
import string
pattern = re.compile(f"[{re.escape(string.punctuation)}]")
punct_remover = str.maketrans("", "", string.punctuation)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger_eng')
function_words = set(stopwords.words('english'))

def WordTokenize(String:str, remove_punc = False):
    if remove_punc:
        String = String.translate(punct_remover)
    tokens = tokenize.word_tokenize(String)
    return tokens
def CharTokenize(String:str,  remove_punc = False):
    if remove_punc:
        String = String.translate(punct_remover)
    tokens = list(String)
    return tokens
def PuncTokenize(String:str):
    return pattern.findall(String)
def SentenceTokenize(String:str):
    return tokenize.sent_tokenize(String)
def TotalTokenize(String: str):
    return list(String)

def PosTokenize(String: str, tag='universal'):
    return nltk.pos_tag(WordTokenize(String), tagset=tag)
def FunctionWordTokenize(String:str):
    """lower case pls"""
    words = WordTokenize(String)
    return [f for f in words if f in function_words]

