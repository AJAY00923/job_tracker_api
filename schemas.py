from pydantic import BaseModel
from typing import Optional

class JobApplicationCreate(BaseModel):
    company : str
    role : str
    status : Optional[str] = "applied"

class JobApplicationUpdate(BaseModel):
    status : str
    
class UserLogin(BaseModel):
    username : str
    password : str

class Token(BaseModel):
    access_token : str
    token_type : str