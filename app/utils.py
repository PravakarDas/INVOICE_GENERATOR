"""
Utility functions for invoice management.
Handles date formatting, file cleanup, and session management.
"""

import os
import time
from datetime import date
from flask import session
from config import Config


def format_date(value: date) -> str:
    """Format date to DD/MM/YYYY."""
    return value.strftime("%d/%m/%Y")


def cleanup_old_invoices(max_age_seconds: int = 3600):
    """
    Remove invoice PDFs older than specified age.
    
    Args:
        max_age_seconds: Maximum age of files to keep (default: 1 hour)
    """
    try:
        if not os.path.exists(Config.OUTPUT_DIR):
            return
        
        current_time = time.time()
        
        for filename in os.listdir(Config.OUTPUT_DIR):
            if filename.endswith('.pdf'):
                file_path = os.path.join(Config.OUTPUT_DIR, filename)
                
                # Check file age
                file_age = current_time - os.path.getmtime(file_path)
                
                if file_age > max_age_seconds:
                    try:
                        os.remove(file_path)
                    except OSError:
                        pass  # Skip if file is in use or can't be deleted
    except Exception:
        pass  # Silently fail to avoid breaking the app


def cleanup_session_invoice():
    """
    Clean up invoice file associated with current session.
    Called when user navigates back to form or refreshes.
    """
    try:
        filename = session.get('invoice_filename')
        
        if filename:
            file_path = os.path.join(Config.OUTPUT_DIR, filename)
            
            if os.path.exists(file_path):
                try:
                    os.remove(file_path)
                except OSError:
                    pass
            
            # Clear session data
            session.pop('invoice_filename', None)
            session.pop('invoice_data', None)
    except Exception:
        pass


def ensure_output_directory():
    """Ensure the output directory exists."""
    os.makedirs(Config.OUTPUT_DIR, exist_ok=True)

