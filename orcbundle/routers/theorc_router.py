from typing import Annotated, Any
from fastapi import APIRouter, Body

from orcbundle.models.bundle import Bundle, OrcRequest
from orcbundle.services.theorc import start_theorc_workflow

theorc_router = APIRouter(
    prefix="/theorc",
    responses={404: {"description": "Not found"}},
    tags=["theorc"]
)



@theorc_router.post("/",)
async def start_orc_workflow(
    orc_request: Annotated[OrcRequest, Body()]
):

    
    result = await start_theorc_workflow(orc_request.model_dump())
    print()
    return "Workflow started"