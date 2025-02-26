import streamlit as st
import asyncio
import os
from src.report import generate_report_pdf, generate_report_image, generate_report_text
from src.agents.agent_chat import (
    chat_cardiologist, chat_oncologist, chat_neurologist, chat_endocrinologist,
    chat_pulmonologist, chat_nephrologist, chat_gastroenterologist, chat_hematologist,
    chat_rheumatologist, chat_dermatologist, chat_ophthalmologist, chat_otolaryngologist,
    chat_urologist, chat_gynecologist, chat_obstetrician, chat_orthopedic_surgeon,
    chat_pediatrician, chat_psychiatrist, chat_geriatrist, chat_infectious_disease_specialist,
    chat_allergist_immunologist, chat_anesthesiologist, chat_radiologist, chat_pathologist
)
from src.utils.report_generator import generate_medical_report

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False


def login():
    if st.session_state.logged_in:
        main_page()
    else:
        st.title("Login Page")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if username == "admin" and password == "admin":
                st.success("Login successful")
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.session_state.logged_in = False
                st.error("Invalid username or password")


async def main_page():
    st.title("Medigent AI")
    option = st.sidebar.selectbox(
        "Select an option", ["Get Report", "Chat with Specialist"])
    if option == "Get Report":
        await get_report()
    elif option == "Chat with Specialist":
        await chat_with_specialist()


# Ensure temp directory exists
TEMP_DIR = "temp"
os.makedirs(TEMP_DIR, exist_ok=True)


async def get_report():
    st.title("Get Report")
    report_type = st.selectbox("Select the type of report", [
                               "PDF", "Image", "Text"])

    if report_type == "PDF":
        lab_report_pdf = st.file_uploader(
            "Upload lab report PDF", type=["pdf"])
        scan_report_pdf = st.file_uploader(
            "Upload scan report PDF", type=["pdf"])

        if st.button("Generate Report"):
            with st.spinner("Generating report..."):
                if lab_report_pdf and scan_report_pdf:
                    lab_pdf_path = os.path.join(TEMP_DIR, lab_report_pdf.name)
                    scan_pdf_path = os.path.join(
                        TEMP_DIR, scan_report_pdf.name)

                    # Save files to temp directory
                    with open(lab_pdf_path, "wb") as f:
                        f.write(lab_report_pdf.read())
                    with open(scan_pdf_path, "wb") as f:
                        f.write(scan_report_pdf.read())

                    report = await generate_report_pdf(lab_pdf_path, scan_pdf_path)
                    generate_medical_report(report)
                    # download pdf
                    st.download_button(
                        label="Download Report", data=open("medical_report.pdf", "rb").read(), file_name="medical_report.pdf", mime="application/pdf"
                    )
                else:
                    st.error("Please upload both lab report and scan report")

    elif report_type == "Image":
        lab_report_image = st.file_uploader(
            "Upload lab report Image", type=["png", "jpg", "jpeg"])
        scan_report_image = st.file_uploader(
            "Upload scan report Image", type=["png", "jpg", "jpeg"])

        if st.button("Generate Report"):
            with st.spinner("Generating report..."):
                if lab_report_image and scan_report_image:
                    lab_image_path = os.path.join(
                        TEMP_DIR, lab_report_image.name)
                    scan_image_path = os.path.join(
                        TEMP_DIR, scan_report_image.name)

                    # Save files to temp directory
                    with open(lab_image_path, "wb") as f:
                        f.write(lab_report_image.read())
                    with open(scan_image_path, "wb") as f:
                        f.write(scan_report_image.read())

                    report = await generate_report_image(lab_image_path, scan_image_path)
                    st.write(report)
                else:
                    st.error("Please upload both lab report and scan report")

    elif report_type == "Text":
        lab_report_text = st.text_area("Enter lab report text")
        scan_report_text = st.text_area("Enter scan report text")

        if st.button("Generate Report"):
            with st.spinner("Generating report..."):
                if lab_report_text and scan_report_text:
                    report = await generate_report_text(lab_report_text, scan_report_text)
                    st.write(report)
                else:
                    st.error("Please enter both lab report and scan report")


async def chat_with_specialist():
    specialists = [
        "Cardiologist",
        "Oncologist",
        "Neurologist",
        "Endocrinologist",
        "Pulmonologist",
        "Nephrologist",
        "Gastroenterologist",
        "Hematologist",
        "Rheumatologist",
        "Dermatologist",
        "Ophthalmologist",
        "Otolaryngologist",
        "Urologist",
        "Gynecologist",
        "Obstetrician",
        "Orthopedic_Surgeon",
        "Pediatrician",
        "Psychiatrist",
        "Geriatrist",
        "Infectious_Disease_Specialist",
        "Allergist_Immunologist",
        "Anesthesiologist",
        "Radiologist",
        "Pathologist"
    ]

    st.title("Chat with Specialist")
    specialist = st.selectbox("Select a specialist", specialists)

    # create a unique chat session id for each chat
    chat_id = specialist

    # create a chat session state
    if chat_id not in st.session_state:
        st.session_state[chat_id] = []

    # Display chat messages from history on app rerun
    for message in st.session_state[chat_id]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("Ask your specialist..."):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state[chat_id].append({"role": "user", "content": prompt})

        response = "Hey this is a response from the specialist"
        # Display assistant response in chat message container
        with st.chat_message(f"{specialist}"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state[chat_id].append(
            {"role": f"{specialist}", "content": response})

if __name__ == "__main__":
    if st.session_state.logged_in:
        asyncio.run(main_page())
    else:
        login()
