from fastapi import FastAPI
from app.route import base_router

app = FastAPI()


#Routes
app.include_router(base_router)