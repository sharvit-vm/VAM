from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime, UTC

class DocumentInput(BaseModel):
    filename: str
    content: str

class EnrichmentResult(BaseModel):
    language: Optional[str] = None

class ProcessingResult(BaseModel):
    filename: str
    word_count: int = Field(ge=0)
    file_type: str
    language: Optional[str] = None
    processing_time_ms: float
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))