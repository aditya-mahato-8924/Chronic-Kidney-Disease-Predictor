from pydantic import BaseModel, Field
from typing import Annotated, Literal

class UserInput(BaseModel):

    age: Annotated[int, Field(..., description="Age of the patient in years", ge=1, le=120)]

    bp: Annotated[int, Field(..., description="Blood Pressure in mm/Hg", ge=50, le=200)]

    sg: Annotated[float, Field(..., description="Specific gravity of urine (normal: 1.005–1.030)", ge=1.005, le=1.030)]

    al: Annotated[int, Field(..., description="Albumin level in urine (0 = normal, higher values indicate kidney issues)", ge=0, le=5)]

    su: Annotated[int, Field(..., description="Sugar level in urine (0 = normal, higher values indicate glucose in urine)", ge=0, le=5)]

    pc: Annotated[
        Literal["not present", "present"],
        Field(description="Pus Cells in urine. 'present' indicates infection or inflammation")
    ]

    pcc: Annotated[
        Literal["not present", "present"],
        Field(description="Pus Cell Clumps in urine. Presence may indicate severe urinary infection")
    ]

    ba: Annotated[
        Literal["not present", "present"],
        Field(description="Bacteria detected in urine sample")
    ]

    bgr: Annotated[int, Field(..., description="Random Blood Glucose level in mg/dL", ge=40, le=500)]

    bu: Annotated[int, Field(..., description="Blood Urea level in mg/dL (higher values may indicate kidney dysfunction)", ge=5, le=200)]

    sc: Annotated[float, Field(..., description="Serum Creatinine in mg/dL (important indicator of kidney function)", ge=0.1, le=15.0)]

    hemo: Annotated[float, Field(..., description="Hemoglobin level in g/dL", ge=3.0, le=20.0)]

    htn: Annotated[
        Literal["yes", "no"],
        Field(description="Whether the patient has hypertension (high blood pressure)")
    ]

    dm: Annotated[
        Literal["yes", "no"],
        Field(description="Whether the patient has diabetes mellitus")
    ]

    cad: Annotated[
        Literal["yes", "no"],
        Field(description="Whether the patient has coronary artery disease (heart disease)")
    ]

    appet: Annotated[
        Literal["good", "poor"],
        Field(description="Patient's appetite condition")
    ]

    pe: Annotated[
        Literal["yes", "no"],
        Field(description="Pedal edema: swelling in legs or feet")
    ]

    ane: Annotated[
        Literal["yes", "no"],
        Field(description="Anemia: condition where hemoglobin level is low")
    ]