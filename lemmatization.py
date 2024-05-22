import nltk 
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')
nltk.download('omw-1.4')


def lemma(text):
    lemmatizer = WordNetLemmatizer()
    lemmatized_list = []

    for key in text.keys():
        lemmatized_key = lemmatizer.lemmatize(key)
        lemmatized_list.append(lemmatized_key)
    return lemmatized_list

