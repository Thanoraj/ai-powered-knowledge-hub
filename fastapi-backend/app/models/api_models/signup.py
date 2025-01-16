from pydantic import BaseModel


class Signup(BaseModel):
    name: str
    email: str
    password: str
