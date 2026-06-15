"""
Prediction service — swap in a real model here.
"""

from typing import List


def run_prediction(features: List[float]) -> float:
    """
    Placeholder predictor. Replace with sklearn/PyTorch model inference.

    Parameters
    ----------
    features : List[float]
        Input feature vector.

    Returns
    -------
    float
        Model prediction.
    """
    # TODO: load model and run inference
    return sum(features)  # placeholder
