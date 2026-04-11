# from fastapi import FastAPI
# from app.routes.router import api_router
# from mangum import Mangum

# # from app.core.database import Base, engine
# # Base.metadata.create_all(bind=engine)


# app = FastAPI(
#     title="IFAHMS API",
#     root_path="/default/ifahms-lambda"
# )


# @app.get("/")
# def root():
#     return {"message": "API WORKING 🚀"}

# @app.get("/test")
# def test():
#     return {"ok": True}


# app.include_router(api_router, prefix="/api")

# handler = Mangum(app, api_gateway_base_path="/default/ifahms-lambda")

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

@app.get("/test")
def test():
    return {"ok": True}

app.include_router(api_router, prefix="/api")

handler = Mangum(app, lifespan="off")
