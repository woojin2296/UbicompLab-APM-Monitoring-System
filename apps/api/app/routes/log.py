from datetime import datetime, timezone
from flask import Blueprint, jsonify, request

from ..services.state import create_log_entry, get_logs

bp = Blueprint("log", __name__)


@bp.route("/log", methods=["GET", "POST"])
def log_route():
    if request.method == "POST":
        payload = request.get_json(silent=True) or {}
        incident_id = payload.get("incident_id")
        service = payload.get("service")
        status = payload.get("status", "unknown")
        message = payload.get("message", "")

        log = create_log_entry(
            timestamp=datetime.now(timezone.utc).isoformat(),
            incident_id=incident_id,
            service=service,
            status=status,
            message=message,
        )
        return jsonify(log), 201

    return jsonify(get_logs()), 200
