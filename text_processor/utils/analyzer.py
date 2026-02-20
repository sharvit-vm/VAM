from config import MAX_WORD_LENGTH

def count_words(text: str) -> int:
    return len(text.split())

def unique_words(text: str):
    return {word for word in text.split()}

def filter_long_words(text: str):
    return [
        word for word in text.split()
        if len(word) > MAX_WORD_LENGTH
    ]