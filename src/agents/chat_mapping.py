from src.agents.agent_chat import *


async def call_chat_agents(patient_data, user_query, specialist):
    if specialist == "Cardiologist":
        result = await chat_cardiologist(user_query, patient_data)
        return result
    elif specialist == "Oncologist":
        result = await chat_oncologist(user_query, patient_data)
        return result
    elif specialist == "Neurologist":
        result = await chat_neurologist(user_query, patient_data)
    elif specialist == "Radiologist":
        result = await chat_radiologist(user_query, patient_data)
    elif specialist == "Pathologist":
        result = await chat_pathologist(user_query, patient_data)
        return result
    elif specialist == "Endocrinologist":
        result = await chat_endocrinologist(user_query, patient_data)
        return result
    elif specialist == "Gynecologist":
        result = await chat_gynecologist(user_query, patient_data)
    elif specialist == "Geriatrist":
        result = await chat_geriatrist(user_query, patient_data)
        return result
    elif specialist == "Allergist_Immunologist":
        result = await chat_allergist_immunologist(user_query, patient_data)
        return result
    elif specialist == "Anesthesiologist":
        result = await chat_anesthesiologist(user_query, patient_data)
        return result
    elif specialist == "Infectious_Disease_Specialist":
        result = await chat_infectious_disease_specialist(user_query, patient_data)
        return result
    elif specialist == "Pulmonologist":
        result = await chat_pulmonologist(user_query, patient_data)
        return result
    elif specialist == "Gastroenterologist":
        result = await chat_gastroenterologist(user_query, patient_data)
        return result
    elif specialist == "Nephrologist":
        result = await chat_nephrologist(user_query, patient_data)
        return result
    elif specialist == "Dermatologist":
        result = await chat_dermatologist(user_query, patient_data)
        return result
    elif specialist == "Hematologist":
        result = await chat_hematologist(user_query, patient_data)
        return result
    elif specialist == "Urologist":
        result = await chat_urologist(user_query, patient_data)
        return result
    elif specialist == "Orthopedic_Surgeon":
        result = await chat_orthopedic_surgeon(user_query, patient_data)
        return result
    elif specialist == "Ophthalmologist":
        result = await chat_ophthalmologist(user_query, patient_data)
        return result
    elif specialist == "Otolaryngologist":
        result = await chat_otolaryngologist(user_query, patient_data)
        return result
    elif specialist == "Pediatrician":
        result = await chat_pediatrician(user_query, patient_data)
        return result
    elif specialist == "Psychiatrist":
        result = await chat_psychiatrist(user_query, patient_data)
    elif specialist == "Obstetrician":
        result = await chat_obstetrician(user_query, patient_data)
        return result
    elif specialist == "Rheumatologist":
        result = await chat_rheumatologist(user_query, patient_data)
        return result
    else:
        return ""
