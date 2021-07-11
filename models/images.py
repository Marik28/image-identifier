from pydantic import BaseModel


class Decision(BaseModel):
    filename: str
    appropriate: bool
    liked: bool
