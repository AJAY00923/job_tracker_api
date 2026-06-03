from pydantic import BaseModel
from typing import Optional

class JobApplicationCreate(BaseModel):
    company : str
    role : str
    status : Optional[str] = "applied"

class JobApplicationUpdate(BaseModel):
    status : str
    