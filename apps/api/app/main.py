from flask import Flask
from .routes.log import bp as log_bp
from .routes.incident import bp as incident_bp
from .routes.health import bp as health_bp
from .services.state import initialize_state


def create_app() -> Flask:
    app = Flask(__name__)

    initialize_state()

    app.register_blueprint(log_bp)
    app.register_blueprint(incident_bp)
    app.register_blueprint(health_bp)

    return app
