from pydantic import BaseModel, EmailStr

class BaseUserModel(BaseModel):
    name : str = None
    email : EmailStr = None

class ReqUserModel(BaseUserModel):
    password : str

class ResUserModel(BaseUserModel):
    id: int