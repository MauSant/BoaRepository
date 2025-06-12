from typing import Annotated
from fastapi import APIRouter, Body

from orcbundle.models.bundle_from_publication import PublicationData
from orcbundle.services.domain_crud import domain_crud
from orcbundle.models.domain import Domain

domain_router = APIRouter(
    prefix="/domains",
    responses={404: {"description": "Not found"}},
    tags=["domain"]
)

@domain_router.get("/",)
async def read_domain(file_name):
    domain = domain_crud.read_one(file_name=id)
    e = Domain.model_validate(domain)
    return domain

@domain_router.get("/all",)
async def read_all_domain():
    domains = domain_crud.read_all()
    return domains


# @domain_router.post("/",)
# async def create_domain(domain: Annotated[Domain, Body()]) -> Domain:
#     created_domain = domain_crud.create(domain.model_dump())
#     return created_domain

# @domain_router.post("/build",)
# async def build_domain(domain: Annotated[PublicationData, Body()]) -> Domain:
#     print()
#     builded_domain = domain_crud.build_from_publication(domain)
#     return builded_domain