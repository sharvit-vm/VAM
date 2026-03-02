from pydantic import BaseModel, Field
class Keyword(BaseModel):
    word: str
    score: float = Field(ge=0, le=1)