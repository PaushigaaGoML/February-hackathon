import os
from openai import OpenAI
from pdf2image import convert_from_path
import base64
from io import BytesIO
from src.schema.response_schema import LabReportResponse, ImagingReportResponse


# Load API key from environment variable and initiate openai class
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI()


def pdf_to_image(pdf_path):
    images = convert_from_path(pdf_path)
    base64_images = []

    for image in images:
        image = image.convert("RGB")
        buffer = BytesIO()
        image.save(buffer, format="JPEG")
        encoded_string = base64.b64encode(buffer.getvalue()).decode("utf-8")
        base64_images.append(encoded_string)

    return base64_images

# Function to extract text from PDF


def extract_patient_data_pdf(pdf_path: str, report_type: str):
    images = pdf_to_image(pdf_path=pdf_path)
    patient_data = {}
    for image in images:
        if report_type == "lab report":
            response = client.beta.chat.completions.parse(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": "Extract the test details from the image provided. Strictly do not miss out any test detail. Extract only the test details, not patient details. If any of the information is not provided, leave it as an empty string. Strictly do not provide a value that is not present in the lab report image."},
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{image}",
                                },
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
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{image}",
                                },
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
