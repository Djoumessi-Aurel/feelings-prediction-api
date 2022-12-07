from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import RegexpTokenizer
from cleaning import cleaning, remove_freqwords
import pickle

with open("modeles", 'rb') as file:
    models_dic = pickle.load(file)


def tokenize_text(text):
    token = RegexpTokenizer(r'[a-zA-Z0-9]+')
    cv = CountVectorizer(stop_words='english',ngram_range = (1,1),tokenizer = token.tokenize)
    return cv.fit_transform([text])


def predict_sentiment(text, modelname):
    text = cleaning(text)
    text = remove_freqwords(text)
    t_text = tokenize_text(text)
    
    nbcol = models_dic[modelname]['nbcol']
    model = models_dic[modelname]['model']
    
    t_text.resize((1,nbcol))
    result = model.predict(t_text)[0]
    proba = model.predict_proba(t_text)[0]
    
    if(result==0):
        message = f'Ce commentaire est négatif à {round(100*proba[0], 2)}% '
        
    elif(result==1):
        message = f'Ce commentaire est positif à {round(100*proba[1], 2)}% '
    
    message += f"d'après la méthode {models_dic[modelname]['name']}"
    
    return result, proba, message
    