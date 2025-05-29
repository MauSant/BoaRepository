from pydantic import BaseModel, Field, Json
from typing import Any

class ProcessInfo(BaseModel):
    title: str
    author: str
    version: str
    description: str

class activity(BaseModel):
    alias: str
    json: Json[Any]
    name: str

class PublicationData(BaseModel):
    process_info: ProcessInfo = Field(alias="processInfo")
    activities: list[activity]
