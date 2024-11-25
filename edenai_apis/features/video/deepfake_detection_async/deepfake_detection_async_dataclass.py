from typing import Literal
from pydantic import BaseModel, Field


class DeepfakeDetectionAsyncDataClass(BaseModel):
    average_score: float = Field(ge=0, le=1)
    prediction: Literal["ai-generated", "original"]
    details_per_frame: list

    @staticmethod
    def set_label_based_on_score(ai_score: float):
        if ai_score > 0.5:
            return "ai-generated"
        else:
            return "original"
