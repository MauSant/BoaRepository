from typing import Annotated
from fastapi import APIRouter, Body

from orcbundle.services.bundle_crud import bundle_crud
from orcbundle.models.bundle import Bundle

bundle_router = APIRouter(
    prefix="/bundles",
    responses={404: {"description": "Not found"}},
    tags=["bundles"]
)

@bundle_router.get("/",)
async def read_bundle(id):
    bundle = bundle_crud.read_one(item_id=id)
    e = Bundle.model_validate(bundle)
    return bundle

@bundle_router.get("/all",)
async def read_all_bundle():
    bundles = bundle_crud.read_all()
    return bundles

@bundle_router.post("/",)
async def create_bundle(bundle: Annotated[Bundle, Body()]):
    created_bundle = bundle_crud.create(bundle.model_dump())
    return created_bundle