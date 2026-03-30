import asyncio
import time
from app.models.schemas import ProcessingResult
from app.processors.txt_processor import TxtProcessor
from app.processors.pdf_processor import PdfProcessor
from app.processors.docx_processor import DocxProcessor
from app.services.language_service import LanguageService


class DocumentPipeline:
    def __init__(self):
        self.language_service = LanguageService()

    def get_processor(self, filepath):
        if filepath.suffix == ".txt":
            return TxtProcessor(filepath)
        elif filepath.suffix == ".pdf":
            return PdfProcessor(filepath)
        elif filepath.suffix == ".docx":
            return DocxProcessor(filepath)
        else:
            raise ValueError("Unsupported file type")

    async def process_file(self, filepath):
        start_time = time.perf_counter()
        processor = self.get_processor(filepath)
        text = processor.extract_text()
        language = await self.language_service.detect_language(text)
        end_time = time.perf_counter()
        processing_time_ms = (end_time - start_time) * 1000
        return ProcessingResult(filename=filepath.name, word_count=processor.word_count(text),file_type=filepath.suffix,language=language,
        processing_time_ms=processing_time_ms,)

    async def run(self, files):
        tasks = [self.process_file(file) for file in files]
        return await asyncio.gather(*tasks) 