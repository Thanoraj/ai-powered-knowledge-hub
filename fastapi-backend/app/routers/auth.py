from fastapi import APIRouter, Response, status

from app.controllers.auth_controller import signup_user
from app.models.api_models.signin import Signin
from app.models.api_models.signup import Signup

router = APIRouter()


@router.post("/signup", tags=["auth"])
def signup(signup: Signup, response: Response):
    """
    Credentials based sign up
    """
    signup_user(signup)
    response.status_code = status.HTTP_200_OK
    return {"message": "Logged in successfully"}


@router.post("/signin", tags=["auth"])
def signin(signin: Signin, response: Response):
    print(signin)
    response.status_code = status.HTTP_200_OK
    return {"message": "Logged in successfully"}
