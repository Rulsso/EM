from collections import Counter
def build_vocabulary(text):
  
    # Crear un conjunto de palabras únicas
    vocabulary = Counter()
    for word in text:
        vocabulary.update(word.split())
    #print(vocabulary)
    return vocabulary
