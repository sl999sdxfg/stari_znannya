from enum import StrEnum
from datetime import date, datetime
from dataclasses import dataclass
from typing import Optional
from sqlmodel import Field, SQLModel
import uuid


def generate_uuid():
    """Generate a unique UUID for a user."""
    return str(uuid.uuid4())

@dataclass
class Status(StrEnum):
    PARENT = 'parent'
    STUDENT = 'student'
    TEACHER = 'teacher'

class UserBase(SQLModel):
    """Base model for user data."""
    name: str = Field(index=True)
    middle_name: str = Field(index=True)
    surname: str = Field(index=True)
    school: str = Field()
    birthday: date = ''
    last_visit: datetime = ''
    status: Status = ''