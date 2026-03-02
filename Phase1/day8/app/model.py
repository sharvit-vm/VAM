from pydantic import BaseModel, Field
class LLMRequest(BaseModel):
    prompt: str
    temperature: float = Field(default=0.7, ge=0, le=1)

class LLMResponse(BaseModel):
    content: str
    total_tokens: int