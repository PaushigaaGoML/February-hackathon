from pydantic import BaseModel, Field
from typing import List, Literal


class LabReportResponseSchema(BaseModel):
    test_name: str = Field(..., description="Name of the laboratory test",
                           example="Hemoglobin")
    result: str = Field(..., description="Result of the test",
                        example="13.5 g/dL")
    reference_range: str = Field(
        ..., description="Normal reference range for the test", example="12-16 g/dL")
    notes: str = Field(..., description="Additional notes regarding the test",
                       example="Normal levels observed")


class LabReportResponse(BaseModel):
    lab_report: List[LabReportResponseSchema] = Field(
        ..., description="List of lab test results")


class ImagingReportSchema(BaseModel):
    test_name: str = Field(..., description="Name of the imaging test",
                           example="MR Angiogram, Neck, W/O Contrast")
    findings: str = Field(..., description="Detailed findings from the imaging study",
                          example="No significant stenosis, tortuosity in bilateral internal carotid arteries, preserved vertebral basilar system, 0.4 cm right thyroid nodule.")
    impression: str = Field(..., description="Summary or conclusion of the findings",
                            example="Normal MRA with no significant issues.")
    signed_by: str = Field(..., description="Doctor's name and date of report signing",
                           example="Kathryn Dean (April 23, 2024)")


class ImagingReportResponse(BaseModel):
    imaging_reports: List[ImagingReportSchema] = Field(
        ..., description="List of imaging test reports")


class PriorityListResponseSchema(BaseModel):
    specialist: Literal[
        "Cardiologist", "Neurologist", "Oncologist", "Endocrinologist",
        "Pulmonologist", "Nephrologist", "Gastroenterologist", "Hematologist",
        "Rheumatologist", "Dermatologist", "Ophthalmologist", "Otolaryngologist",
        "Urologist", "Gynecologist", "Obstetrician", "Orthopedic Surgeon",
        "Pediatrician", "Psychiatrist", "Geriatrician", "Infectious Disease Specialist",
        "Allergist_Immunologist", "Anesthesiologist", "Radiologist", "Pathologist"
    ] = Field(..., description="Name of the specialist", example="Cardiologist")

    reason: str = Field(
        ...,
        description="Reason for assigning the specialist",
        example="High risk of heart disease from the provided patient data"
    )
    priority_level: Literal["urgent", "high", "moderate", "low"] = Field(
        ...,
        description="Priority level of the specialist",
        example="urgent"
    )


class PriorityListResponse(BaseModel):
    priority_order: List[PriorityListResponseSchema] = Field(
        ..., description="List of specialists ordered by priority")


class SpecialistResponse(BaseModel):
    key_findings: list[str] = Field(..., description="List of key findings from the patient's medical history", example=[
                                    "Elevated LDL cholesterol levels (160 mg/dL).", "Blood pressure recorded at 150/95 mmHg (hypertensive range)."])
    identified_risks_and_concerns: list[str] = Field(..., description="List of identified risks and concerns", example=[
                                                     "Arrhythmia risk due to premature ventricular contractions.", "Possibility of early-stage left ventricular dysfunction."])
    cross_speciality_interaction: List[Literal[
        "Cardiologist", "Neurologist", "Oncologist", "Endocrinologist",
        "Pulmonologist", "Nephrologist", "Gastroenterologist", "Hematologist",
        "Rheumatologist", "Dermatologist", "Ophthalmologist", "Otolaryngologist",
        "Urologist", "Gynecologist", "Obstetrician", "Orthopedic Surgeon",
        "Pediatrician", "Psychiatrist", "Geriatrician", "Infectious Disease Specialist",
        "Allergist_Immunologist", "Anesthesiologist", "Radiologist", "Pathologist"
    ]] = Field(..., description="List of interactions with other specialists", example=["Endocrinologist", "Nephrologist"])
    recommended_further_tests_or_consultations: list[str] = Field(..., description="List of recommended further tests or consultations", example=[
                                                                  "Echocardiographic follow-up in 3 months."])
    potential_treatment_suggestions: list[str] = Field(..., description="List of potential treatment suggestions", example=[
                                                       "Initiate antihypertensive therapy with an ACE inhibitor.", "Prescribe statins to lower LDL cholesterol.", "Lifestyle modifications: low-sodium, heart-healthy diet"])


class ChatResponse(BaseModel):
    chat_response: str = Field(..., description="Response from the chat agent",
                               example="Hello! How can I assist you today?")
