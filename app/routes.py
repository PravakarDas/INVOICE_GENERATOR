"""
Route handlers for invoice generation workflow.
Manages form submission, PDF generation, downloads, and cleanup.
"""

import uuid
import os
from flask import (
    Blueprint, render_template, redirect, url_for, 
    send_file, session, flash, request
)
from app.forms import InvoiceForm
from app.models import Invoice, ExpenseItem
from app.pdf_generator import generate_invoice_pdf
from app.utils import cleanup_old_invoices, cleanup_session_invoice

invoice_bp = Blueprint("invoice", __name__)


@invoice_bp.before_request
def cleanup_before_request():
    """Clean up old invoices and session data before each request."""
    cleanup_old_invoices()
    
    # Clean up previous invoice on page refresh
    if request.path == "/" and request.method == "GET":
        cleanup_session_invoice()


@invoice_bp.route("/", methods=["GET", "POST"])
def invoice_form():
    """Display invoice form and handle submission."""
    form = InvoiceForm()
    
    # Debug: Print request method and form data
    print(f"Request method: {request.method}")
    print(f"Form data: {request.form}")
    print(f"Form expenses count: {len(form.expenses)}")

    if form.validate_on_submit():
        try:
            print("Form validation passed!")
            
            # Build expense items from form data
            expenses = [
                ExpenseItem(
                    date=item.form.date.data,
                    category=item.form.category.data,
                    description=item.form.description.data,
                    note=item.form.note.data or "",
                    amount=float(item.form.amount.data),
                )
                for item in form.expenses
            ]
            
            print(f"Expenses built: {len(expenses)} items")

            # Validate at least one expense exists
            if not expenses:
                flash("Please add at least one expense item.", "error")
                return render_template("invoice_form.html", form=form)

            # Create invoice object
            invoice = Invoice(
                company=form.company.data,
                prepared_by=form.prepared_by.data,
                employee_id=form.employee_id.data,
                department=form.department.data,
                start_date=form.start_date.data,
                end_date=form.end_date.data,
                expenses=expenses,
            )

            # Generate custom filename: startdate_enddate_preparedby_company
            start_str = invoice.start_date.strftime('%m%d%Y')
            end_str = invoice.end_date.strftime('%m%d%Y')
            prepared_by_clean = invoice.prepared_by.replace(' ', '')
            company_clean = invoice.company.replace(' ', '')
            filename = f"{start_str}_{end_str}_{prepared_by_clean}_{company_clean}.pdf"
            
            print(f"Generating PDF: {filename}")
            
            # Generate PDF
            pdf_path = generate_invoice_pdf(invoice, filename)
            
            print(f"PDF generated at: {pdf_path}")
            
            # Store filename in session for download
            session['invoice_filename'] = filename
            session['invoice_data'] = {
                'company': invoice.company,
                'prepared_by': invoice.prepared_by,
                'date_range': f"{invoice.start_date.strftime('%d/%m/%Y')} - {invoice.end_date.strftime('%d/%m/%Y')}",
                'total': invoice.total_amount
            }

            flash("Invoice generated successfully!", "success")
            return redirect(url_for("invoice.invoice_preview"))
            
        except Exception as e:
            print(f"Error during invoice generation: {e}")
            import traceback
            traceback.print_exc()
            flash(f"Error generating invoice: {str(e)}", "error")
            return render_template("invoice_form.html", form=form)
    
    # Show form validation errors
    if request.method == "POST":
        print(f"Form validation failed. Errors: {form.errors}")
        if form.errors:
            for field, errors in form.errors.items():
                for error in errors:
                    flash(f"{field}: {error}", "error")

    return render_template("invoice_form.html", form=form)


@invoice_bp.route("/preview")
def invoice_preview():
    """Display preview page with download link."""
    filename = session.get('invoice_filename')
    invoice_data = session.get('invoice_data', {})
    
    if not filename:
        flash("No invoice generated. Please create a new invoice.", "warning")
        return redirect(url_for("invoice.invoice_form"))
    
    return render_template(
        "invoice_preview.html", 
        filename=filename,
        invoice_data=invoice_data
    )


@invoice_bp.route("/download/<filename>")
def download_invoice(filename):
    """Download the generated invoice PDF."""
    # Security: Only allow downloading the session's invoice
    if session.get('invoice_filename') != filename:
        flash("Invalid download request.", "error")
        return redirect(url_for("invoice.invoice_form"))
    
    from config import Config
    pdf_path = os.path.join(Config.OUTPUT_DIR, filename)
    
    if not os.path.exists(pdf_path):
        flash("Invoice file not found.", "error")
        return redirect(url_for("invoice.invoice_form"))
    
    return send_file(
        pdf_path,
        as_attachment=True,
        download_name=filename
    )
