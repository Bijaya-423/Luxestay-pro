
from fastapi import FastAPI
from app.routes.router import api_router
from mangum import Mangum

app = FastAPI(
    title="IFAHMS API",
    docs_url="/docs",
    redoc_url="/redoc"
)

@app.get("/")
def root():
    return {"message": "API WORKING 🚀"}

# @app.get("/test")
# def test():
#     return {"ok": True}

app.include_router(api_router, prefix="/api")

handler = Mangum(app, lifespan="off")



