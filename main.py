"""
FastAPI application entrypoint.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes import health, predict

app = FastAPI(
    title="python-api-projects",
    description="ML inference and REST API experiments",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, prefix="/health", tags=["Health"])
app.include_router(predict.router, prefix="/predict", tags=["Predict"])


@app.get("/")
def root():
    return {"status": "ok", "message": "API is running"}
