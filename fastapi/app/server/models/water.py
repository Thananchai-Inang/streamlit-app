from typing import Optional
from pydantic import BaseModel, Field


class WaterSchema(BaseModel):
    name: str = Field(...)
    day: int = Field(..., gt=0)
    waterlevel: float = Field(..., ge=0.0)
    waterdrain: float = Field(..., ge=0.0)

    class Config:
        schema_extra = {
            "example": {
                "name": "M7",
                "day":13,
                "waterlevel":121.1,
                "waterdrain":102.4,
            }
        }


class UpdateWaterModel(BaseModel):
    name: Optional[str]
    day: Optional[int]
    waterlevel: Optional[float]
    waterdrain: Optional[float]

    class Config:
        schema_extra = {
            "example": {
                "name": "M7",
                "day":13,
                "waterlevel":121.1,
                "waterdrain":102.4,
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}