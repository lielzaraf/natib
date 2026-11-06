"""Gradio interface for submitting and viewing resident requests."""

from datetime import datetime

import gradio as gr

from natib.analysis import analyze_request
from natib.models import MissingField, Request, RequestAnalysis


_FIELD_LABELS = {
    MissingField.ADDRESS: "כתובת",
    MissingField.INCIDENT_TYPE: "סוג המפגע",
    MissingField.DETAILS: "פרטים על המפגע",
}
_URGENCY_LABELS = {"low": "נמוכה", "medium": "בינונית", "high": "גבוהה"}


def format_analysis(analysis: RequestAnalysis) -> str:
    """Format a structured analysis as Hebrew text for the interface.

    Args:
        analysis: The structured result returned by the analysis module.

    Returns:
        A readable Hebrew summary of the request and any missing information.
    """
    address = analysis.address or "לא צוין"
    incident_type = analysis.incident_type or "לא צוין"
    summary = analysis.summary or "לא ניתן להפיק תיאור קצר"
    urgency = _URGENCY_LABELS[analysis.urgency.value] if analysis.urgency else "לא נקבעה"
    urgency_reason = analysis.urgency_reason or "לא נמסר הסבר"

    lines = [
        f"כתובת: {address}",
        f"סוג המפגע: {incident_type}",
        f"סיכום: {summary}",
        f"דחיפות: {urgency}",
        f"הסבר לדחיפות: {urgency_reason}",
    ]
    if analysis.missing_fields:
        missing = ", ".join(_FIELD_LABELS[field] for field in analysis.missing_fields)
        lines.append(f"מידע להשלמה: {missing}")
    else:
        lines.append("מידע להשלמה: אין")

    return "\n".join(lines)


def analyze_text(text: str) -> str:
    """Submit text for analysis and return its formatted result.

    Args:
        text: The free-form request entered by the resident.

    Returns:
        A Hebrew presentation of the analysis result.
    """
    request = Request(text=text, received_at=datetime.now().astimezone())
    return format_analysis(analyze_request(request))


demo = gr.Interface(
    fn=analyze_text,
    inputs=gr.Textbox(label="תיאור המפגע", lines=5, placeholder="תארו את המפגע", rtl=True),
    outputs=gr.Textbox(label="סיכום הפנייה", lines=7, rtl=True),
    title="דיווח על מפגע",
    flagging_mode="never",
)


def main() -> None:
    """Launch the Gradio interface in a local browser."""
    demo.launch()


if __name__ == "__main__":
    main()