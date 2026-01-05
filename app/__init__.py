"""
Flask application factory and initialization.
Creates and configures the Flask application instance.
"""

import os
from flask import Flask
from config import Config


def create_app() -> Flask:
    """
    Create and configure Flask application.
    
    Returns:
        Flask: Configured Flask application instance
    """
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    app = Flask(
        __name__,
        template_folder=os.path.join(base_dir, "templates"),
        static_folder=os.path.join(base_dir, "static"),
    )

    # Load configuration
    app.config.from_object(Config)

    # Ensure output directory exists
    os.makedirs(app.config['OUTPUT_DIR'], exist_ok=True)

    # Register blueprints
    from app.routes import invoice_bp
    app.register_blueprint(invoice_bp)

    return app

