from datetime import datetime, timezone
from flask import Blueprint, jsonify, request

from ..services.state import (
    create_incident,
    get_incidents,
    get_incident,
    update_incident,
)
from ..services.events import broadcast_incident_event

bp = Blueprint("incident", __name__)


@bp.route("/incident", methods=["GET", "POST"])
def incident_collection():
    if request.method == "POST":
        payload = request.get_json(silent=True) or {}
        incident = create_incident(
            service=payload.get("service", "unknown"),
            detail=payload.get("detail", ""),
            status=payload.get("status", "Noticed"),
        )
        broadcast_incident_event("on_outage", incident)
        return jsonify(incident), 201

    return jsonify(get_incidents()), 200


@bp.route("/incident/<int:incident_id>", methods=["PATCH"])
def incident_detail(incident_id: int):
    payload = request.get_json(silent=True) or {}
    current = get_incident(incident_id)
    if current is None:
        return jsonify({"error": "incident not found"}), 404

    status = payload.get("status")
    detail = payload.get("detail")

    updated = update_incident(
        incident_id=incident_id,
        status=status,
        detail=detail,
    )

    if status == "Restored":
        updated["restoredAt"] = datetime.now(timezone.utc).isoformat()
        broadcast_incident_event("on_recovered", updated)

    return jsonify(updated), 200
