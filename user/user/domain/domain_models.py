from typing import Optional

from core.utils import VyaparBaseModel
from user.types import UserId



class UserDomainModel(VyaparBaseModel):
    id: Optional[UserId] = None
    name: str
    contact_number: str
    aadhar_number: str
    pan_number: str
    is_setup_completed: bool

    class Config:
        orm_mode = True
