from autogen_agentchat import agents
from src.agents.agent_models import chat_model_client
import json

cardiologist = agents.AssistantAgent(
    name="Cardiologist",
    model_client=chat_model_client,
    system_message="""
      You are a **Cardiologist Agent** responsible for providing the response for patient's query related to cardiology.
      Your task is to address the user query and provide relevant information related to patient data and user query.
      """,
)

oncologist = agents.AssistantAgent(
    name="Oncologist",
    model_client=chat_model_client,
    system_message="""
      You are a **Oncologist Agent** responsible for providing the response for patient's query related to oncology.
      Your task is to address the user query and provide relevant information related to patient data and user query.
      """,
)

neurologist = agents.AssistantAgent(
    name="Neurologist",
    model_client=chat_model_client,
    system_message="""
      You are a **Neurologist Agent** responsible for providing the response for patient's query related to Neurology.
      Your task is to address the user query and provide relevant information related to patient data and user query.
      """,
)

endocrinologist = agents.AssistantAgent(
    name="Endocrinologist",
    model_client=chat_model_client,
    system_message="""
      You are a **Endocrinologist Agent** responsible for providing the response for patient's query related to Endocrinology.
      Your task is to address the user query and provide relevant information related to patient data and user query.
      """,
)

pulmonologist = agents.AssistantAgent(
    name="Pulmonologist",
    model_client=chat_model_client,
    system_message="""
      You are a **Pulmonologist Agent** responsible for providing the response for patient's query related to Pulmonology.
      Your task is to address the user query and provide relevant information related to patient data and user query.
      """,
)

nephrologist = agents.AssistantAgent(
    name="Nephrologist",
    model_client=chat_model_client,
    system_message="""
      You are a **Nephrologist Agent** responsible for providing the response for patient's query related to Nephrology.
      Your task is to address the user query and provide relevant information related to patient data and user query.
      """,
)

gastroenterologist = agents.AssistantAgent(
    name="Gastroenterologist",
    model_client=chat_model_client,
    system_message="""
      You are a **Gastroenterologist Agent** responsible for providing the response for patient's query related to Gastroenterology.
      Your task is to address the user query and provide relevant information related to patient data and user query.
      """,
)

hematologist = agents.AssistantAgent(
    name="Hematologist",
    model_client=chat_model_client,
    system_message="""
      You are a **Hematologist Agent** responsible for providing the response for patient's query related to Hematology.
      Your task is to address the user query and provide relevant information related to patient data and user query.
      """,
)

rheumatologist = agents.AssistantAgent(
    name="Rheumatologist",
    model_client=chat_model_client,
    system_message="""
      You are a **Rheumatologist Agent** responsible for providing the response for patient's query related to Rheumatology.
      Your task is to address the user query and provide relevant information related to patient data and user query.
      """,
)

dermatologist = agents.AssistantAgent(
    name="Dermatologist",
    model_client=chat_model_client,
    system_message="""
      You are a **Dermatologist Agent** responsible for providing the response for patient's query related to Dermatology.
      Your task is to address the user query and provide relevant information related to patient data and user query.
      """,
)

ophthalmologist = agents.AssistantAgent(
    name="Ophthalmologist",
    model_client=chat_model_client,
    system_message="""
      You are a **Ophthalmologist Agent** responsible for providing the response for patient's query related to Ophthalmology.
      Your task is to address the user query and provide relevant information related to patient data and user query.
      """,
)

otolaryngologist = agents.AssistantAgent(
    name="Otolaryngologist",
    model_client=chat_model_client,
    system_message="""
      You are a **Otolaryngologist Agent** responsible for providing the response for patient's query related to Otolaryngology.
      Your task is to address the user query and provide relevant information related to patient data and user query.
      """,
)

urologist = agents.AssistantAgent(
    name="Urologist",
    model_client=chat_model_client,
    system_message="""
      You are a **Urologist Agent** responsible for providing the response for patient's query related to Urology.
      Your task is to address the user query and provide relevant information related to patient data and user query.
      """,
)

gynecologist = agents.AssistantAgent(
    name="Gynecologist",
    model_client=chat_model_client,
    system_message="""
      You are a **Gynecologist Agent** responsible for providing the response for patient's query related to Gynecology.
      Your task is to address the user query and provide relevant information related to patient data and user query.
      """,
)

obstetrician = agents.AssistantAgent(
    name="Obstetrician",
    model_client=chat_model_client,
    system_message="""
      You are a **Obstetrician Agent** responsible for providing the response for patient's query related to Obstetrics.
      Your task is to address the user query and provide relevant information related to patient data and user query.
      """,
)

orthopedic_surgeon = agents.AssistantAgent(
    name="Orthopedic_Surgeon",
    model_client=chat_model_client,
    system_message="""
      You are a **Orthopedic_Surgeon Agent** responsible for providing the response for patient's query related to Orthopedics.
      Your task is to address the user query and provide relevant information related to patient data and user query.
      """,
)

pediatrician = agents.AssistantAgent(
    name="Pediatrician",
    model_client=chat_model_client,
    system_message="""
      You are a **Pediatrician Agent** responsible for providing the response for patient's query related to Pediatrics.
      Your task is to address the user query and provide relevant information related to patient data and user query.
      """,
)

psychiatrist = agents.AssistantAgent(
    name="Psychiatrist",
    model_client=chat_model_client,
    system_message="""
      You are a **Psychiatrist Agent** responsible for providing the response for patient's query related to Psychiatry.
      Your task is to address the user query and provide relevant information related to patient data and user query.
      """,
)

geriatrist = agents.AssistantAgent(
    name="Geriatrist",
    model_client=chat_model_client,
    system_message="""
      You are a **Geriatrist Agent** responsible for providing the response for patient's query related to Geriatry.
      Your task is to address the user query and provide relevant information related to patient data and user query.
      """,
)

infectious_disease_specialist = agents.AssistantAgent(
    name="Infectious_Disease_Specialist",
    model_client=chat_model_client,
    system_message="""
      You are a **Infectious_Disease_Specialist Agent** responsible for providing the response for patient's query related to Infectious_Disease_Speciality.
      Your task is to address the user query and provide relevant information related to patient data and user query.
      """,
)

allergist_immunologist = agents.AssistantAgent(
    name="Allergist_Immunologist",
    model_client=chat_model_client,
    system_message="""
      You are a **Allergist_Immunologist Agent** responsible for providing the response for patient's query related to Allergy_Immunology.
      Your task is to address the user query and provide relevant information related to patient data and user query.
      """,
)

anesthesiologist = agents.AssistantAgent(
    name="Anesthesiologist",
    model_client=chat_model_client,
    system_message="""
      You are a **Anesthesiologist Agent** responsible for providing the response for patient's query related to Anesthesiology.
      Your task is to address the user query and provide relevant information related to patient data and user query.
      """,
)

radiologist = agents.AssistantAgent(
    name="Radiologist",
    model_client=chat_model_client,
    system_message="""
      You are a **Radiologist Agent** responsible for providing the response for patient's query related to Radiology.
      Your task is to address the user query and provide relevant information related to patient data and user query.
      """,
)

pathologist = agents.AssistantAgent(
    name="Pathologist",
    model_client=chat_model_client,
    system_message="""
      You are a **Pathologist Agent** responsible for providing the response for patient's query related to Pathology.
      Your task is to address the user query and provide relevant information related to patient data and user query.
      """,
)


async def chat_cardiologist(user_query, patient_data):
    task = f"User query: {user_query}\nPatient Data: {json.dumps(patient_data, indent=4)}"
    result = await cardiologist.run(task=task)
    return result.messages[-1].content


async def chat_oncologist(user_query, patient_data):
    task = f"User query: {user_query}\nPatient Data: {json.dumps(patient_data, indent=4)}"
    result = await oncologist.run(task=task)
    return result.messages[-1].content


async def chat_neurologist(user_query, patient_data):
    task = f"User query: {user_query}\nPatient Data: {json.dumps(patient_data, indent=4)}"
    result = await neurologist.run(task=task)
    return result.messages[-1].content


async def chat_radiologist(user_query, patient_data):
    task = f"User query: {user_query}\nPatient Data: {json.dumps(patient_data, indent=4)}"
    result = await radiologist.run(task=task)
    return result.messages[-1].content


async def chat_pathologist(user_query, patient_data):
    task = f"User query: {user_query}\nPatient Data: {json.dumps(patient_data, indent=4)}"
    result = await pathologist.run(task=task)
    return result.messages[-1].content


async def chat_endocrinologist(user_query, patient_data):
    task = f"User query: {user_query}\nPatient Data: {json.dumps(patient_data, indent=4)}"
    result = await endocrinologist.run(task=task)
    return result.messages[-1].content


async def chat_gynecologist(user_query, patient_data):
    task = f"User query: {user_query}\nPatient Data: {json.dumps(patient_data, indent=4)}"
    result = await gynecologist.run(task=task)
    return result.messages[-1].content


async def chat_geriatrist(user_query, patient_data):
    task = f"User query: {user_query}\nPatient Data: {json.dumps(patient_data, indent=4)}"
    result = await geriatrist.run(task=task)
    return result.messages[-1].content


async def chat_allergist_immunologist(user_query, patient_data):
    task = f"User query: {user_query}\nPatient Data: {json.dumps(patient_data, indent=4)}"
    result = await allergist_immunologist.run(task=task)
    return result.messages[-1].content


async def chat_anesthesiologist(user_query, patient_data):
    task = f"User query: {user_query}\nPatient Data: {json.dumps(patient_data, indent=4)}"
    result = await anesthesiologist.run(task=task)
    return result.messages[-1].content


async def chat_infectious_disease_specialist(user_query, patient_data):
    task = f"User query: {user_query}\nPatient Data: {json.dumps(patient_data, indent=4)}"
    result = await infectious_disease_specialist.run(task=task)
    return result.messages[-1].content


async def chat_pulmonologist(user_query, patient_data):
    task = f"User query: {user_query}\nPatient Data: {json.dumps(patient_data, indent=4)}"
    result = await pulmonologist.run(task=task)
    return result.messages[-1].content


async def chat_gastroenterologist(user_query, patient_data):
    task = f"User query: {user_query}\nPatient Data: {json.dumps(patient_data, indent=4)}"
    result = await gastroenterologist.run(task=task)
    return result.messages[-1].content


async def chat_nephrologist(user_query, patient_data):
    task = f"User query: {user_query}\nPatient Data: {json.dumps(patient_data, indent=4)}"
    result = await nephrologist.run(task=task)
    return result.messages[-1].content


async def chat_dermatologist(user_query, patient_data):
    task = f"User query: {user_query}\nPatient Data: {json.dumps(patient_data, indent=4)}"
    result = await dermatologist.run(task=task)
    return result.messages[-1].content


async def chat_hematologist(user_query, patient_data):
    task = f"User query: {user_query}\nPatient Data: {json.dumps(patient_data, indent=4)}"
    result = await hematologist.run(task=task)
    return result.messages[-1].content


async def chat_urologist(user_query, patient_data):
    task = f"User query: {user_query}\nPatient Data: {json.dumps(patient_data, indent=4)}"
    result = await urologist.run(task=task)
    return result.messages[-1].content


async def chat_psychiatrist(user_query, patient_data):
    task = f"User query: {user_query}\nPatient Data: {json.dumps(patient_data, indent=4)}"
    result = await psychiatrist.run(task=task)
    return result.messages[-1].content


async def chat_rheumatologist(user_query, patient_data):
    task = f"User query: {user_query}\nPatient Data: {json.dumps(patient_data, indent=4)}"
    result = await rheumatologist.run(task=task)
    return result.messages[-1].content


async def chat_ophthalmologist(user_query, patient_data):
    task = f"User query: {user_query}\nPatient Data: {json.dumps(patient_data, indent=4)}"
    result = await ophthalmologist.run(task=task)
    return result.messages[-1].content


async def chat_obstetrician(user_query, patient_data):
    task = f"User query: {user_query}\nPatient Data: {json.dumps(patient_data, indent=4)}"
    result = await obstetrician.run(task=task)
    return result.messages[-1].content


async def chat_pediatrician(user_query, patient_data):
    task = f"User query: {user_query}\nPatient Data: {json.dumps(patient_data, indent=4)}"
    result = await pediatrician.run(task=task)
    return result.messages[-1].content


async def chat_otolaryngologist(user_query, patient_data):
    task = f"User query: {user_query}\nPatient Data: {json.dumps(patient_data, indent=4)}"
    result = await otolaryngologist.run(task=task)
    return result.messages[-1].content


async def chat_orthopedic_surgeon(user_query, patient_data):
    task = f"User query: {user_query}\nPatient Data: {json.dumps(patient_data, indent=4)}"
    result = await orthopedic_surgeon.run(task=task)
    return result.messages[-1].content
