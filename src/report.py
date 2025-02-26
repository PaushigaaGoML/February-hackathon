from src.utils.pdf_parser import extract_patient_data_pdf
from src.utils.image_parser import extract_patient_data_image
from src.utils.text_parser import extract_patient_data_text

from src.agents.general_practioner_agent import determine_priority
from src.agents.agent_orchestration import get_report_from_specialist
import json


async def generate_report_pdf(lab_report_pdf_path, scan_report_pdf_path):
    # extract patient data out of it
    patient_data = {}
    lab_data = extract_patient_data_pdf(lab_report_pdf_path, 'lab report')
    scan_data = extract_patient_data_pdf(scan_report_pdf_path, 'image report')
    patient_data['lab report'] = lab_data
    patient_data['image report'] = scan_data

    # get priority order
    priority_order = await determine_priority(patient_data)
    priority_order = json.loads(priority_order)
    print(priority_order)

    # get report according to the priority
    report = await get_report_from_specialist(priority_order, patient_data)

    # get cross speciality interaction value and check if it is present in the priority order. If not present, get the report from the specialist
    print(report)
    return report


async def generate_report_image(lab_report_image_path, scan_report_image_path):
    # extract patient data out of it
    patient_data = {}
    lab_data = extract_patient_data_image(lab_report_image_path, 'lab report')
    scan_data = extract_patient_data_image(
        scan_report_image_path, 'image report')
    patient_data['lab report'] = lab_data
    patient_data['image report'] = scan_data

    # get priority order
    priority_order = await determine_priority(patient_data)

    # get report according to the priority
    report = await get_report_from_specialist(priority_order, patient_data)
    return report


async def generate_report_text(lab_report_text, scan_report_text):
    # extract patient data out of it
    patient_data = {}
    lab_data = extract_patient_data_text(lab_report_text, 'lab report')
    scan_data = extract_patient_data_text(scan_report_text, 'image report')
    patient_data['lab report'] = lab_data
    patient_data['image report'] = scan_data

    # get priority order
    priority_order = await determine_priority(patient_data)

    # get report according to the priority
    report = await get_report_from_specialist(priority_order, patient_data)
    return report
