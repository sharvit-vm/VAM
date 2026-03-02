from utils.cleaner import clean_text
from utils.analyzer import (
    count_words,
    unique_words,
    filter_long_words
)

def main():
    try:
        text = input("Enter text: ")
        cleaned = clean_text(text)
        print("Word count:", count_words(cleaned))
        print("Unique words:", unique_words(cleaned))
        print("Long words:", filter_long_words(cleaned))
    except Exception as e:
        print("Error:", e)
if __name__ == "__main__":
    main()