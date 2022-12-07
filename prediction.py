from nltk.stem import WordNetLemmatizer
from cleaning import cleaning, remove_freqwords
import pickle

with open("modeles", 'rb') as file:
    models_dic = pickle.load(file)


def predict_sentiment(text, modelname):
    text = cleaning(text)
    text = remove_freqwords(text)

    wordnet_lem = WordNetLemmatizer()
    text = wordnet_lem.lemmatize(text)

    cv = models_dic[modelname]['cv']
    t_text = cv.transform([text])
    
    model = models_dic[modelname]['model']
    
    result = model.predict(t_text)[0]
    proba = model.predict_proba(t_text)[0]
    
    if(result==0):
        message = f'Ce commentaire est négatif à {round(100*proba[0], 2)}% '
        
    elif(result==1):
        message = f'Ce commentaire est positif à {round(100*proba[1], 2)}% '
    
    message += f"d'après la méthode {models_dic[modelname]['name']}"
    
    return result, proba, message
