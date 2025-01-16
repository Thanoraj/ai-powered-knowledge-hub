from pydantic import BaseModel


class Signin(BaseModel):
    email: str
    password: str
