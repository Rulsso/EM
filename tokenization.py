import spacy

nlp = spacy.load("es_core_news_sm")

def text_tokenization(text):  
    # Process the text
    doc = nlp(text)
    # Extract sentences
    tokens = [token.text for token in doc]
    #print(sentences)
    return tokens
