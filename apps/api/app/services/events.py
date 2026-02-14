from __future__ import annotations

from typing import Any, Dict


def broadcast_incident_event(event_name: str, incident: Dict[str, Any]) -> None:
    """
    WebSocket / Slack / external broker event hook.

    TODO: connect broker (Socket.IO/Redis/PubSub) and structured logging.
    """
    # keep API contract-compatible side effects in one place for easy extension
    _ = event_name, incident
