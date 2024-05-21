import re
from bs4 import BeautifulSoup

def clean_text(text):
    # Convert text to lower case
    text = text.lower()
    # Delete special characters, except space using a regular expresion 
    text = re.sub(r'[^\w\s]', '', text)
    # Delete numbers
    text = re.sub(r'\d+', '', text)
    # Delete extra spaces
    text = ' '.join(text.split())
    return text

def extract_and_clean_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        # Read HTML content 
        content = file.read()
        # Extract text with BeautifulSoup
        soup = BeautifulSoup(content, 'html.parser')
        text = soup.get_text()

        cleaned_text = clean_text(text)

        #print(cleaned_text)

        return cleaned_text
