from pydantic import BaseModel
from pathlib import Path


class FileResult(BaseModel):
    filename: str
    word_count: int
    extension: str

    @classmethod
    def from_path(cls, path: Path, content: str) -> "FileResult":
        return cls(
            filename=path.name,
            word_count=len(content.split()),
            extension=path.suffix,
        )