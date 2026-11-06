"""Analyze resident requests and return a structured result."""

from natib.models import Request, RequestAnalysis, Urgency


def analyze_request(request: Request) -> RequestAnalysis:
    """Return a fixed example analysis for a resident request.

    Args:
        request: The resident's request. Its text is not analyzed by this stub.

    Returns:
        A sample structured analysis, to be replaced later by an LLM-backed
        implementation without changing this function's interface.
    """
    return RequestAnalysis(
        address="רחוב הרצל 12",
        incident_type="פנס רחוב",
        summary="פנס הרחוב אינו פועל.",
        urgency=Urgency.MEDIUM,
        urgency_reason="מדובר בתקלה בתאורת רחוב שאינה מתוארת כמסכנת חיים.",
        missing_fields=(),
    )