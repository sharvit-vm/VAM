from .base import BaseProcessor
from docx import Document

class DocxProcessor(BaseProcessor):
    def extract_text(self) -> str:
        doc = Document(self.filepath)
        return "\n".join([p.text for p in doc.paragraphs])