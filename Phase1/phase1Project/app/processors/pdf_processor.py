from .base import BaseProcessor
from PyPDF2 import PdfReader


class PdfProcessor(BaseProcessor):
    def extract_text(self) -> str:
        reader = PdfReader(self.filepath)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text