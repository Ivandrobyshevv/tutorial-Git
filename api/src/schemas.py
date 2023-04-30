from datetime import date
from typing import List

from pydantic import BaseModel


class CreateAnimal(BaseModel):
    name: str
    birthday: date
    commands: List[str] = []
    genus_name: str
