import string
def clean_text(text: str)->str: 
    if not text.strip():
        raise ValueError("Input string cannot be empty")
    return text.translate(
        str.maketrans('','',string.punctuation)
    ).lower()