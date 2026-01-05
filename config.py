"""
Configuration settings for Invoice Generator application.
Defines environment variables, paths, and app settings.
"""

import os


class Config:
    """Application configuration class."""
    
    # Secret key for session management
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key-change-in-production")
    
    # Base directories
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    OUTPUT_DIR = os.path.join(BASE_DIR, "output", "invoices")
    
    # Session configuration
    SESSION_TYPE = 'filesystem'
    PERMANENT_SESSION_LIFETIME = 3600  # 1 hour
    SESSION_COOKIE_SECURE = False  # Set to True in production with HTTPS
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    
    # File cleanup settings
    CLEANUP_MAX_AGE = 3600  # Remove PDFs older than 1 hour (in seconds)
    
    # WTForms settings
    WTF_CSRF_ENABLED = True
    WTF_CSRF_TIME_LIMIT = None  # No time limit for CSRF tokens
    
    # Upload settings (if needed in future)
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max upload size

