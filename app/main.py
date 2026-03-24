# Entry point of FastAPI app

from fastapi import FastAPI
from app.routes.router import api_router
from app.core.database import Base, engine

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="IFAHMS API")

app.include_router(api_router, prefix="/api")

@app.get("/")
def root():
    return {"message": "IFAHMS Backend Running 🚀"}