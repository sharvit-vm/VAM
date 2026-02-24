from pydantic import BaseModel, Field, model_validator, computed_field
from typing import List
from datetime import datetime
from .keyword import Keyword
class ExtractionResult(BaseModel):
    filename: str
    summary: str
    keywords: List[Keyword]
    generated_at: datetime = Field(default_factory=datetime.utcnow)
    @model_validator(mode="after")
    def validate_keywords_limit(self):
        if len(self.keywords) == 0:
            raise ValueError("At least one keyword required")
        return self
    @computed_field
    @property
    def average_score(self) -> float:
        return round(
            sum(k.score for k in self.keywords) / len(self.keywords),
            2
        )