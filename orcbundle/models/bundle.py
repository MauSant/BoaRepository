
from enum import StrEnum
from typing import Any, Literal, Optional


from pydantic import BaseModel

class ActionTypes(StrEnum):
    HTTP = "HTTP"
    WORKFLOW = "WORKFLOW"
    MESSAGE = "MESSAGE" 

class HTTPMethods(StrEnum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE" 
    PATCH = "PATCH" 

class Action(BaseModel):
    name: str


class HttpAction(Action):
    action_type: Literal[ActionTypes.HTTP]
    url: str
    http_method: HTTPMethods
    # mock: Optional[MockResponse]
    mock: dict[str, Any] = {}
    headers: dict[str, Any] = {}
    query: dict[str, Any] = {}
    form_data: dict[str, Any] = {}
    json: dict[str, Any] = {}
    output: dict[str, Any] = {}
    # auth: dict[str, Any] #TODO disable for now for security reasons. I think we should scope THe Orc for intra organization

class WorkflowAction(Action):
    action_type: Literal[ActionTypes.WORKFLOW]
    queue: str
    parameters: dict[str,Any]
    output: dict[str, Any]
    workflow_configs: dict[str, Any]

class ActionInSteps(BaseModel):
    name:str
    actions:list[str]

class Bundle(BaseModel):
    name: str
    steps: list[ActionInSteps] 
    services: dict[str, HttpAction]
    auth: Optional[str] = "" #TODO