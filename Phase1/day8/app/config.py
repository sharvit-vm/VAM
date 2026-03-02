import os
from dotenv import load_dotenv
from pydantic import BaseModel, ValidationError

load_dotenv()


class Settings(BaseModel):
    api_key: str
    base_url: str
    model: str

    @classmethod
    def load(cls) -> "Settings":
        try:
            return cls(
                api_key=os.getenv("API_KEY"),
                base_url=os.getenv("BASE_URL"),
                model=os.getenv("MODEL"),
            )
        except ValidationError as e:
            raise ValueError("Invalid environment configuration") from e