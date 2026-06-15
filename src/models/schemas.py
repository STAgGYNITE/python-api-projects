from pydantic import BaseModel
from typing import List


class PredictRequest(BaseModel):
    features: List[float]

    model_config = {
        "json_schema_extra": {
            "examples": [{"features": [1.0, 2.3, 0.5, 4.1]}]
        }
    }


class PredictResponse(BaseModel):
    prediction: float | int | str
