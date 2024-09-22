from typing import List
from pydantic import BaseModel

from user.types import UserId


class UserDomainModel(BaseModel):
    id: UserId
    name: str
    contact_number: str
    aadhar_number: str
    pan_number: str
    is_setup_completed: bool

    class Config:
        orm_mode = True
