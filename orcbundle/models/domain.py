from enum import StrEnum
from typing import Any, Literal, Optional
from orcbundle.models.bundle import HttpAction

from pydantic import BaseModel

class Activities(BaseModel):
    name: str
    id: str
    services:dict[str, HttpAction]


class Role(BaseModel):
    name: str 
    id: str
    activites: list[Activities]
    

class Domain(BaseModel):
    name: str
    id: str
    roles: list[Role]