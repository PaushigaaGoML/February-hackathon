from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
import json


def generate_medical_report(data, filename="medical_report.pdf"):
    doc = SimpleDocTemplate(filename, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    title_style = ParagraphStyle(
        "TitleStyle",
        parent=styles["Title"],
        fontSize=18,
        spaceAfter=12,
        textColor=colors.darkblue
    )

    section_header_style = ParagraphStyle(
        "SectionHeaderStyle",
        parent=styles["Heading2"],
        fontSize=14,
        spaceBefore=10,
        spaceAfter=6,
        textColor=colors.darkred
    )

    text_style = styles["BodyText"]
    text_style.spaceAfter = 6

    for specialty, details in data.items():
        details = json.loads(details)

        story.append(Paragraph(specialty, title_style))
        story.append(Spacer(1, 10))

        for section, items in details.items():
            section_name = section.replace("_", " ").title()
            story.append(Paragraph(section_name, section_header_style))

            if isinstance(items, list):
                for item in items:
                    story.append(Paragraph(f"- {item}", text_style))

            story.append(Spacer(1, 10))

        story.append(Spacer(1, 20))

    doc.build(story)
