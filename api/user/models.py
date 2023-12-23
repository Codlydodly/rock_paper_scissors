from pydantic import BaseModel, validator
from typing import Optional

class UserResponseModel(BaseModel):
    id: int
    username: str