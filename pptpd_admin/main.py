from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas import pptpd


app = FastAPI(
    prefix='/api/v1/'
)

app.include_router(pptpd.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)
