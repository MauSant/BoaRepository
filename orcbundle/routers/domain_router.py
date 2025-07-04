from typing import Annotated
from fastapi import APIRouter, Body

from orcbundle.models.bundle_from_publication import PublicationData
from orcbundle.services.domain_crud import domain_crud
from orcbundle.models.domain import Domain

domain_router = APIRouter(
    prefix="/bpdl",
    responses={404: {"description": "Not found"}},
    tags=["bpdl"]
)

@domain_router.get("/",)
async def read_domain(file_name):
    bpdl = domain_crud.read_one(file_name=id)
    e = Domain.model_validate(bpdl)
    return bpdl

@domain_router.get("/all",)
async def read_all_domain():
    bpdls = domain_crud.read_all()
    return bpdls


# @domain_router.post("/",)
# async def create_domain(domain: Annotated[Domain, Body()]) -> Domain:
#     created_domain = domain_crud.create(domain.model_dump())
#     return created_domain

# @domain_router.post("/build",)
# async def build_domain(domain: Annotated[PublicationData, Body()]) -> Domain:
#     print()
#     builded_domain = domain_crud.build_from_publication(domain)
#     return builded_domain