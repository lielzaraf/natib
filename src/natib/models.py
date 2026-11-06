"""Shared data types for resident requests and their analysis."""

from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class Urgency(str, Enum):
    """Urgency level assigned to a reported issue."""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class MissingField(str, Enum):
    """Resident-provided information that is absent from a request."""

    ADDRESS = "address"
    INCIDENT_TYPE = "incident_type"
    DETAILS = "details"


@dataclass(frozen=True)
class Request:
    """A resident's submitted report.

    Attributes:
        text: The free-form text submitted by the resident.
        received_at: The time the request was received, preferably timezone-aware.
    """

    text: str
    received_at: datetime


@dataclass(frozen=True)
class RequestAnalysis:
    """Structured summary produced from a resident request.

    Attributes:
        address: The reported address, or None if it could not be identified.
        incident_type: The kind of issue, or None if it could not be identified.
        summary: A concise system-generated description, or None if unavailable.
        urgency: The assigned urgency, or None if it could not be determined.
        urgency_reason: Why that urgency was assigned, or None if unavailable.
        missing_fields: Resident-provided details that still need clarification.
    """

    address: str | None
    incident_type: str | None
    summary: str | None
    urgency: Urgency | None
    urgency_reason: str | None
    missing_fields: tuple[MissingField, ...]