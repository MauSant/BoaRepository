
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from orcbundle.routers.bundle_router import bundle_router
from orcbundle.routers.boa_simulator_router import boa_simulator_router
from orcbundle.routers.domain_router import domain_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    #TODO Add database here
    yield

app = FastAPI(
    title="Boa Repository"
)

# app.include_router(bundle_router)
app.include_router(boa_simulator_router)
app.include_router(domain_router)



origins = [
    "http://127.0.0.1:8000",
    "https://127.0.0.1:8000 ",
    "http://localhost"
    "http://localhost:8000",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)