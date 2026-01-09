"""
Form definitions for invoice generation.
Handles user input validation and dynamic expense entry management.
"""

from flask_wtf import FlaskForm
from wtforms import (
    StringField, DecimalField, FieldList, FormField, SelectField, DateField, Form
)
from wtforms.validators import DataRequired, NumberRange


class ExpenseForm(Form):
    """Individual expense entry form (non-CSRF sub-form)."""
    
    date = DateField("Date", validators=[DataRequired()])
    category = SelectField(
        "Category",
        choices = [
            ("Ama Tea Coffee", "Ama Tea Coffee"),
            ("Courier Service", "Courier Service"),
            ("Electricity bill", "Electricity bill"),
            ("Electronic item", "Electronic item"),
            ("Expense from employee", "Expense from employee"),
            ("Internet Bill", "Internet Bill"),
            ("Mobile Recharge", "Mobile Recharge"),
            ("Office Equipment", "Office Equipment"),
            ("Office Event", "Office Event"),
            ("Office Tour", "Office Tour"),
            ("Others", "Others"),
            ("Others bill", "Others bill"),
            ("PiHR", "PiHR"),
            ("Rent", "Rent"),
            ("Servicing", "Servicing"),
            ("Snacks", "Snacks"),
            ("Sports", "Sports"),
            ("Stationary", "Stationary"),
            ("Tax (TDS/VDS)", "Tax (TDS/VDS)"),
            ("Trade License", "Trade License"),
            ("Transportation", "Transportation"),
            ("Travel", "Travel"),
        ]

,
        validators=[DataRequired()],
    )
    description = StringField("Description", validators=[DataRequired()])
    note = StringField("Note")
    amount = DecimalField(
        "Amount", 
        validators=[
            DataRequired(),
            NumberRange(min=0.01, message="Amount must be greater than 0")
        ],
        places=2
    )


class InvoiceForm(FlaskForm):
    """Main invoice form with company details and expense entries."""
    
    company = SelectField(
        "Company",
        choices=[
            ("BitApps", "BitApps"),
            ("BitCode", "BitCode"),
        ],
        validators=[DataRequired()],
    )
    prepared_by = StringField("Prepared By", validators=[DataRequired()])
    employee_id = StringField("Employee ID", validators=[DataRequired()])
    department = SelectField(
        "Department",
        choices=[
            ("Private", "Private"),
            ("HR", "HR"),
        ],
        validators=[DataRequired()],
    )
    start_date = DateField("Start Date", validators=[DataRequired()])
    end_date = DateField("End Date", validators=[DataRequired()])
    expenses = FieldList(FormField(ExpenseForm), min_entries=1)





    
