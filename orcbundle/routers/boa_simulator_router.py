from typing import Annotated, Any
from fastapi import APIRouter, Body, HTTPException

from orcbundle.models.bundle import Bundle, OrcRequest
from orcbundle.services.boa_simulator import start_boa_simulator_workflow

boa_simulator_router = APIRouter(
    prefix="/boa_simulator",
    responses={404: {"description": "Not found"}},
    tags=["BOA Simulator"]
)



@boa_simulator_router.post("/",)
async def start_boas_workflow(
    orc_request: Annotated[OrcRequest, Body()]
    # orc_request: Annotated[dict, Body()]
):
    
    # try:
    #     model = OrcRequest(**orc_request)
    # except Exception as e:
    #     raise HTTPException(status_code=422, detail=str(e))
    # result = await start_boa_simulator_workflow(model.model_dump())
    
    result = await start_boa_simulator_workflow(orc_request.model_dump())
    print()
    return result
   