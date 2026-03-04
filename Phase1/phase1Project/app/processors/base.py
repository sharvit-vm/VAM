from abc import ABC, abstractmethod
class BaseProcessor(ABC):
    def __init__(self, filepath):
        self.filepath = filepath

    @abstractmethod
    def extract_text(self) -> str:
        pass

    def word_count(self, text: str) -> int:
        return len(text.split())