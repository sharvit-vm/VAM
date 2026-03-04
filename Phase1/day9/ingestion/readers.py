import asyncio
from PyPDF2 import PdfReader
from docx import Document
async def read_txt(path: str) -> str:
    def read():
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    return await asyncio.to_thread(read)

async def read_pdf(path: str) -> str:
    def read():
        reader = PdfReader(path)
        return " ".join(page.extract_text() or "" for page in reader.pages)
    return await asyncio.to_thread(read)

async def read_docx(path: str) -> str:
    def read():
        doc = Document(path)
        return " ".join(p.text for p in doc.paragraphs)
    return await asyncio.to_thread(read)