from openai import OpenAI
from src.schema.response_schema import LabReportResponse, ImagingReportResponse
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI()


def extract_patient_data_text(text: str, report_type: str):
    patient_data = {}
    if report_type == "lab report":
        response = client.beta.chat.completions.parse(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Extract the test details from the image provided. Strictly do not miss out any test detail. Extract only the test details, not patient details. If any of the information is not provided, leave it as an empty string. Strictly do not provide a value that is not present in the lab report image."},
                        {
                            "type": "text",
                            "text": f"Input data: {text}"
                        },
                    ],
                }
            ],
            max_tokens=1200,
            response_format=LabReportResponse
        )
        event = response.choices[0].message.parsed
        patient_data.update(event)
    elif report_type == "image report":
        response = client.beta.chat.completions.parse(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Extract the test details from the image provided. Strictly do not miss out any test detail. Extract only the test details, not patient details. If any of the information is not provided, leave it as an empty string. Strictly do not provide a value that is not present in the lab report image."},
                        {
                            "type": "text",
                            "text": f"Input data: {text}"
                        },
                    ],
                }
            ],
            max_tokens=1200,
            response_format=ImagingReportResponse
        )
        event = response.choices[0].message.parsed
        patient_data.update(event)
    if report_type == "lab report":
        patient_data_serializable = {
            "lab_report": [report.model_dump() for report in patient_data["lab_report"]]
        }
        return patient_data_serializable
    elif report_type == "image report":
        patient_data_serializable = {
            "imaging_reports": [report.model_dump() for report in patient_data["imaging_reports"]]
        }
        return patient_data_serializable
