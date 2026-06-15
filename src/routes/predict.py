from fastapi import APIRouter, HTTPException
from src.models.schemas import PredictRequest, PredictResponse
from src.services.predictor import run_prediction

router = APIRouter()


@router.post("/", response_model=PredictResponse)
def predict(request: PredictRequest):
    try:
        result = run_prediction(request.features)
        return PredictResponse(prediction=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
