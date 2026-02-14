from __future__ import annotations

from typing import Any, Dict, List, Optional

_LOGS: List[Dict[str, Any]] = []
_INCIDENTS: Dict[int, Dict[str, Any]] = {}
_COUNTER = 1


def initialize_state() -> None:
    """Initialize in-memory state for local development."""



def create_log_entry(
    *,
    timestamp: str,
    incident_id: int,
    service: str,
    status: str,
    message: str,
) -> Dict[str, Any]:
    item = {
        "timestamp": timestamp,
        "incident_id": incident_id,
        "service": service,
        "status": status,
        "message": message,
    }
    _LOGS.append(item)
    return item


def get_logs() -> List[Dict[str, Any]]:
    return list(_LOGS)


def create_incident(*, service: str, detail: str, status: str) -> Dict[str, Any]:
    global _COUNTER
    incident = {
        "id": _COUNTER,
        "status": status,
        "service": service,
        "detail": detail,
        "occurredAt": None,
        "restoredAt": None,
    }
    _COUNTER += 1
    _INCIDENTS[incident["id"]] = incident
    return incident


def get_incidents() -> List[Dict[str, Any]]:
    return list(_INCIDENTS.values())


def get_incident(incident_id: int) -> Optional[Dict[str, Any]]:
    return _INCIDENTS.get(incident_id)


def update_incident(
    *,
    incident_id: int,
    status: Optional[str] = None,
    detail: Optional[str] = None,
) -> Dict[str, Any]:
    incident = _INCIDENTS[incident_id]
    if status is not None:
        incident["status"] = status
    if detail is not None:
        incident["detail"] = detail
    return incident
