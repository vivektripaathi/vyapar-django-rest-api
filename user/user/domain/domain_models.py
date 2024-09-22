from typing import List

from user.types import UserId
from core.utils import VyaparBaseModel

class UserDomainModel(VyaparBaseModel):
    id: UserId
    name: str
    contact_number: str
    aadhar_number: str
    pan_number: str
    is_setup_completed: bool

    class Config:
        orm_mode = True
