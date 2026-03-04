from .base import BaseProcessor


class TxtProcessor(BaseProcessor):
    def extract_text(self) -> str:
        with open(self.filepath, "r", encoding="utf-8") as f:
            return f.read()