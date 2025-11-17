from pydantic import BaseModel
from typing import Dict, Any


class PredictionInput(BaseModel):
    data: Dict[str, Any]

    class Config:
        schema_extra = {
            "example": {
                "data": {
                    "Reason for absence_0": 0,
                    "Reason for absence_1": 0,
                    "Reason for absence_10": 0,
                    "Reason for absence_11": 0,
                    "Reason for absence_12": 0,
                    "Reason for absence_13": 0,
                    "Reason for absence_14": 0,
                    "Reason for absence_15": 0,
                    "Reason for absence_16": 0,
                    "Reason for absence_17": 0,
                    "Reason for absence_18": 0,
                    "Reason for absence_19": 0,
                    "Reason for absence_21": 0,
                    "Reason for absence_22": 0,
                    "Reason for absence_23": 0,
                    "Reason for absence_24": 0,
                    "Reason for absence_25": 0,
                    "Reason for absence_26": 0,
                    "Reason for absence_27": 0,
                    "Reason for absence_28": 0,
                    "Reason for absence_3": 0,
                    "Reason for absence_4": 0,
                    "Reason for absence_5": 0,
                    "Reason for absence_6": 0,
                    "Reason for absence_7": 0,
                    "Reason for absence_8": 0,
                    "Reason for absence_9": 0,
                    "Month of absence_1": 0,
                    "Month of absence_10": 0,
                    "Month of absence_11": 0,
                    "Month of absence_12": 0,
                    "Month of absence_2": 0,
                    "Month of absence_3": 0,
                    "Month of absence_4": 0,
                    "Month of absence_5": 0,
                    "Month of absence_6": 0,
                    "Month of absence_7": 0,
                    "Month of absence_8": 0,
                    "Month of absence_9": 0,
                    "Day of the week_2": 0,
                    "Day of the week_3": 0,
                    "Day of the week_4": 0,
                    "Day of the week_5": 0,
                    "Day of the week_6": 0,
                    "Seasons_1": 0,
                    "Seasons_2": 0,
                    "Seasons_3": 0,
                    "Seasons_4": 0,
                    "Disciplinary failure_False": 1,
                    "Disciplinary failure_True": 0,
                    "Education_1": 1,
                    "Education_2": 0,
                    "Education_3": 0,
                    "Social drinker_False": 1,
                    "Social drinker_True": 0,
                    "Social smoker_False": 1,
                    "Social smoker_True": 0,
                    "Transportation expense": 200,
                    "Distance from Residence to Work": 10,
                    "Service time": 5,
                    "Age": 30,
                    "Work load Average/day": 250,
                    "Hit target": 95,
                    "Son": 1,
                    "Pet": 0,
                    "Weight": 70,
                    "Height": 170,
                    "Body mass index": 24,
                    "Absenteeism time in hours": 0,
                    "Dependents_count": 1,
                    "Has_dependents": 1,
                    "Lifestyle_risk_score": 5,
                    "Healthy_lifestyle": 1,
                    "Penalty_risk_score": 2,
                    "Reliability_score": 8,
                    "Reliability_score_norm": 0.65,
                    "Workload_deviation": 3
                }
            }
        }


class PredictionOutput(BaseModel):
    prediction: float
