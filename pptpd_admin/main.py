from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas import pptpd


app = FastAPI(
    title='Pptpd-admin API',
    description='Rest-API for fastapi with pptpd server.',
    version='0.1.0',
    prefix='/api/v1/'
)

app.include_router(pptpd.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['GET', 'POST', 'DELETE'],
    allow_headers=['*'],
)
