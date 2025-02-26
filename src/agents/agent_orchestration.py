from src.agents.specialist_agents import *


async def get_report_from_specialist(priority_order, patient_data_serializable):
    specialists = []
    for specialist in priority_order["priority_order"]:
        specialists.append(specialist["specialist"])

    results = {}
    for specialist in specialists:
        if specialist == "Cardiologist":
            result = await call_cardiologist(patient_data_serializable)
            results[specialist] = result
        elif specialist == "Oncologist":
            result = await call_oncologist(patient_data_serializable)
            results[specialist] = result
        elif specialist == "Neurologist":
            result = await call_neurologist(patient_data_serializable)
            results[specialist] = result
        elif specialist == "Radiologist":
            result = await call_radiologist(patient_data_serializable)
            results[specialist] = result
        elif specialist == "Pathologist":
            result = await call_pathologist(patient_data_serializable)
            results[specialist] = result
        elif specialist == "Endocrinologist":
            result = await call_endocrinologist(patient_data_serializable)
            results[specialist] = result
        elif specialist == "Gynecologist":
            result = await call_gynaecologist(patient_data_serializable)
            results[specialist] = result
        elif specialist == "Geriatrist":
            result = await call_geriatrist(patient_data_serializable)
            results[specialist] = result
        elif specialist == "Allergist_Immunologist":
            result = await call_allergist_immunologist(patient_data_serializable)
            results[specialist] = result
        elif specialist == "Anesthesiologist":
            result = await call_anesthesiologist(patient_data_serializable)
            results[specialist] = result
        elif specialist == "Infectious Disease Specialist":
            result = await call_infectious_disease_specialist(patient_data_serializable)
            results[specialist] = result
        elif specialist == "Pulmonologist":
            result = await call_pulmonologist(patient_data_serializable)
            results[specialist] = result
        elif specialist == "Gastroenterologist":
            result = await call_gastroenterologist(patient_data_serializable)
            results[specialist] = result
        elif specialist == "Nephrologist":
            result = await call_nephrologist(patient_data_serializable)
            results[specialist] = result
        elif specialist == "Dermatologist":
            result = await call_dermatologist(patient_data_serializable)
            results[specialist] = result
        elif specialist == "Hematologist":
            result = await call_hematologist(patient_data_serializable)
            results[specialist] = result
        elif specialist == "Urologist":
            result = await call_urologist(patient_data_serializable)
            results[specialist] = result
        elif specialist == "Psychiatrist":
            result = await call_psychiatrist(patient_data_serializable)
            results[specialist] = result
        elif specialist == "Rheumatologist":
            result = await call_rheumatologist(patient_data_serializable)
            results[specialist] = result
        elif specialist == "Opthalmologist":
            result = await call_opthalmologist(patient_data_serializable)
            results[specialist] = result
        elif specialist == "Obstetrician":
            result = await call_obstetrician(patient_data_serializable)
            results[specialist] = result
        elif specialist == "Pediatrician":
            result = await call_pediatrician(patient_data_serializable)
            results[specialist] = result
        elif specialist == "Otolaryngologist":
            result = await call_otolaryngologist(patient_data_serializable)
            results[specialist] = result
        elif specialist == "Orthopedic Surgeon":
            result = await call_orthopedic_surgeon(patient_data_serializable)
            results[specialist] = result
        else:
            results[specialist] = ""
    return results
