from pydantic import BaseModel


class MyData(BaseModel):
    street: str
    housenumber: str
