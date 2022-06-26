from pydantic import BaseModel


class Path(BaseModel):
    source: str
    destination: str