from pydantic import BaseModel


class Book(BaseModel):
    id: str = None
    title: str
    description: str
