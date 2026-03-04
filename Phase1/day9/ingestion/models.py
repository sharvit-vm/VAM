from pydantic import BaseModel, Field
from typing import Literal


class DocumentOutput(BaseModel):
    filename: str
    type: Literal["txt", "pdf", "docx"]
    word_count: int = Field(ge=0)
    content: str