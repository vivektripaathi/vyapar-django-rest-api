from typing import NewType

from pydantic import UUID4

UserId = NewType("UserId", UUID4)
