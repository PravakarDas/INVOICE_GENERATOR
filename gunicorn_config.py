"""Gunicorn configuration for production deployment."""

import os

# Bind to 0.0.0.0 on PORT from environment (required for Render)
bind = f"0.0.0.0:{os.environ.get('PORT', '10000')}"

# Worker configuration
workers = 4
worker_class = "sync"
threads = 2

# Timeout settings
timeout = 120
keepalive = 5

# Logging
accesslog = "-"
errorlog = "-"
loglevel = "info"

# Process naming
proc_name = "invoice_generator"

# Preload app for better performance
preload_app = True
