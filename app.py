"""
AI-Powered Sign Language Detection System
-------------------------------------------
app.py

This is the entry point for the AI microservice (Version 0).

Version 0 Scope:
    - Initialize the Flask application
    - Expose a health-check route ("/")
    - Expose a placeholder prediction route ("/predict")

NOTE:
    No AI/ML inference logic is implemented in this version.
    The "/predict" route currently returns a static JSON response
    indicating that the feature is under development. Real-time
    sign language detection using MediaPipe, OpenCV, and TensorFlow
    will be introduced in later versions (see README.md -> Version Roadmap).

Author: AI + Full Stack Engineering Team
"""

import os
from flask import Flask, jsonify
from dotenv import load_dotenv

# ---------------------------------------------------------------------------
# Environment Configuration
# ---------------------------------------------------------------------------
# Load environment variables from a .env file (if present) into the
# process environment. This allows configuration (port, model path, etc.)
# to be managed outside of source code.
load_dotenv()

FLASK_ENV = os.getenv("FLASK_ENV", "development")
PORT = int(os.getenv("PORT", 5000))
MODEL_PATH = os.getenv("MODEL_PATH", "models/model.h5")

# ---------------------------------------------------------------------------
# Application Factory
# ---------------------------------------------------------------------------
def create_app() -> Flask:
    """
    Application factory function.

    Using a factory pattern (instead of a bare module-level app instance)
    keeps the codebase modular and testable, and makes it easier to plug
    in blueprints, extensions, and configuration objects as the project
    grows in future versions.

    Returns:
        Flask: A configured Flask application instance.
    """
    app = Flask(__name__)

    # Basic app-level configuration.
    # Additional config (DB URIs, secret keys, CORS, etc.) will be added
    # in future versions as the backend and frontend are integrated.
    app.config["MODEL_PATH"] = MODEL_PATH
    app.config["ENV"] = FLASK_ENV

    register_routes(app)

    return app


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------
def register_routes(app: Flask) -> None:
    """
    Registers all HTTP routes for the AI service.

    Keeping route registration in a dedicated function (rather than
    scattering @app.route decorators throughout the file) makes it easy
    to convert these into Flask Blueprints once the project scales.

    Args:
        app (Flask): The Flask application instance to attach routes to.
    """

    @app.route("/", methods=["GET"])
    def health_check():
        """
        Health-check endpoint.

        Used to verify that the AI service is up and running.
        Typically consumed by monitoring tools, load balancers,
        or the Node.js backend in future versions.

        Returns:
            JSON response with service status metadata.
        """
        return jsonify(
            {
                "status": "success",
                "service": "AI Sign Language Detection Service",
                "message": "Service is up and running",
                "version": "0.1.0",
            }
        ), 200

    @app.route("/predict", methods=["POST", "GET"])
    def predict():
        """
        Placeholder prediction endpoint.

        In future versions, this route will:
            1. Accept an image/video frame (or a stream) from the client.
            2. Use MediaPipe to extract hand/pose landmarks.
            3. Feed processed landmarks into a trained TensorFlow model.
            4. Return the predicted sign/gesture as a JSON response.

        For Version 0, this endpoint performs NO inference and simply
        confirms that the route is reachable and under active development.

        Returns:
            JSON response indicating the endpoint's development status.
        """
        return jsonify(
            {
                "status": "success",
                "message": "Prediction endpoint is under development",
                "version": "0.1.0",
            }
        ), 200


# ---------------------------------------------------------------------------
# Entry Point
# ---------------------------------------------------------------------------
app = create_app()

if __name__ == "__main__":
    # debug=True is safe for local development only.
    # This should be disabled (or controlled via FLASK_ENV) in production.
    debug_mode = FLASK_ENV == "development"
    app.run(host="0.0.0.0", port=PORT, debug=debug_mode)
