from dotenv import load_dotenv
import os 
load_dotenv()
MAX_WORD_LENGTH = int(os.getenv("MAX_WORD_LENGTH", 10))