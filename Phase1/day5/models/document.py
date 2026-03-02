from pydantic import BaseModel, Field, field_validator, computed_field
from datetime import datetime
class DocumentInput(BaseModel):
    filename: str = Field(min_length=3)
    content: str
    author: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    @field_validator("content")
    def content_not_empty(cls, value):
        if not value.strip():
            raise ValueError("Document content cannot be empty")
        return value
    @computed_field
    @property
    def word_count(self) -> int:
        return len(self.content.split())