import os
from app import create_app

app = create_app()

if __name__ == "__main__":
    # Get port from environment variable (Render provides PORT)
    port = int(os.environ.get("PORT", 5000))
    
    # Bind to 0.0.0.0 for production deployment (required by Render)
    # Use debug=False in production
    debug_mode = os.environ.get("FLASK_ENV") == "development"
    
    app.run(
        host="0.0.0.0",
        port=port,
        debug=debug_mode
    )
