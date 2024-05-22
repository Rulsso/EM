import data_clean
import tokenization
import file_manager
import vocabulary
import lemmatization
def main():
    # File name 
    file_name = 'e990519_mod.htm'
    text = data_clean.extract_and_clean_text(file_name)
    (text, file_name)
    file_manager.create_file(text,"clean.txt")
    text = tokenization.text_tokenization(text)
    file_manager.create_file_from_list(text,"tokens.txt")
    text = vocabulary.build_vocabulary(text)
    file_manager.create_file_from_list(text,"vocabulary.txt")
    text = lemmatization.lemma(text)
    file_manager.create_file_from_list(text,"lemmas.txt")
    print("done!")

if __name__ == "__main__":
    main()
