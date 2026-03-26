from pydantic import BaseModel
from typing import List

class AnswerSchema(BaseModel):
    answer: str
    sources: List[str]