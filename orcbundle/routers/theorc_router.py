from typing import Annotated, Any
from fastapi import APIRouter, Body, HTTPException

from orcbundle.models.bundle import Bundle, OrcRequest
from orcbundle.services.theorc import start_theorc_workflow

theorc_router = APIRouter(
    prefix="/theorc",
    responses={404: {"description": "Not found"}},
    tags=["theorc"]
)



@theorc_router.post("/",)
async def start_orc_workflow(
    # orc_request: Annotated[OrcRequest, Body()]
    orc_request: Annotated[dict, Body()]
):
    
    try:
        model = OrcRequest(**orc_request)
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))
    
    result = await start_theorc_workflow(model.model_dump())
    print()
    return "Workflow started"
   