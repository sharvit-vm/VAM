from pydantic import BaseModel, Field, field_validator
class ProcessingConfig(BaseModel):
    extract_keywords: bool = True
    max_keywords: int = Field(gt=0, le=5)
    summary_length: int = Field(gt=20, le=300)
    language: str = Field(default="en")
    @field_validator("language")
    def language_supported(cls, value):
        supported = ["en", "fr", "de"]
        if value not in supported:
            raise ValueError(f"Language must be one of {supported}")
        return value