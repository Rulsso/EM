import spacy

def text_tokenization(text):
    nlp = spacy.load("es_core_news_sm")
    # Process the text
    doc = nlp(text)
    # Extract sentences
    sentences = [sent.text for sent in doc.sents]
    #print(sentences)
    return sentences
