"""
Sample test script with 25 expense items
Date range: 01/01/2026 - 01/01/2027
"""

from datetime import date
from app.models import Invoice, ExpenseItem
from app.pdf_generator import generate_invoice_pdf

expenses = [
    ExpenseItem(date=date(2026, 1, 5),  category="Travel",          description="Flight booking",            note="HR meeting",           amount=15000),
    ExpenseItem(date=date(2026, 1, 12), category="Food",            description="Team lunch",               note="",                     amount=4200),
    ExpenseItem(date=date(2026, 1, 20), category="Accommodation",   description="Hotel stay",               note="2 nights",             amount=38000),
    ExpenseItem(date=date(2026, 2, 3),  category="Transportation",  description="Taxi charges",             note="",                     amount=1800),
    ExpenseItem(date=date(2026, 2, 15), category="Other",           description="Office supplies",          note="Stationery",           amount=6200),

    ExpenseItem(date=date(2026, 3, 1),  category="Travel",          description="Train tickets",            note="Client visit",         amount=8900),
    ExpenseItem(date=date(2026, 3, 10), category="Food",            description="Client dinner",            note="",                     amount=12500),
    ExpenseItem(date=date(2026, 3, 25), category="Accommodation",   description="Conference hotel",         note="3 nights",             amount=54000),
    ExpenseItem(date=date(2026, 4, 2),  category="Transportation",  description="Car rental",               note="",                     amount=16000),
    ExpenseItem(date=date(2026, 4, 18), category="Other",           description="Training materials",       note="HR training",          amount=9500),

    ExpenseItem(date=date(2026, 5, 6),  category="Travel",          description="Domestic flight",           note="",                     amount=22000),
    ExpenseItem(date=date(2026, 5, 14), category="Food",            description="Workshop catering",        note="",                     amount=17500),
    ExpenseItem(date=date(2026, 5, 29), category="Accommodation",   description="Guest house",              note="Project stay",         amount=46000),
    ExpenseItem(date=date(2026, 6, 7),  category="Transportation",  description="Fuel reimbursement",       note="",                     amount=7800),
    ExpenseItem(date=date(2026, 6, 21), category="Other",           description="Software license",         note="HR tools",             amount=120000),

    ExpenseItem(date=date(2026, 7, 5),  category="Travel",          description="International flight",     note="",                     amount=185000),
    ExpenseItem(date=date(2026, 7, 16), category="Food",            description="Business lunch",           note="",                     amount=6800),
    ExpenseItem(date=date(2026, 8, 2),  category="Accommodation",   description="Resort stay",              note="Annual meet",          amount=72000),
    ExpenseItem(date=date(2026, 8, 19), category="Transportation",  description="Airport transfer",         note="",                     amount=3500),
    ExpenseItem(date=date(2026, 9, 3),  category="Other",           description="Event registration",       note="",                     amount=25000),

    ExpenseItem(date=date(2026, 10, 11), category="Travel",         description="Regional travel",          note="",                     amount=14500),
    ExpenseItem(date=date(2026, 11, 6),  category="Food",           description="Team dinner",              note="Festival",             amount=9800),
    ExpenseItem(date=date(2026, 11, 22), category="Accommodation",  description="Hotel booking",            note="",                     amount=41000),
    ExpenseItem(date=date(2026, 12, 10), category="Transportation", description="Cab services",             note="",                     amount=5200),
    ExpenseItem(date=date(2027, 1, 1),   category="Other",          description="Year-end supplies",        note="",                     amount=30500),
]

invoice = Invoice(
    company="BitApps",
    prepared_by="John Doe",
    employee_id="EMP001",
    department="HR",
    start_date=date(2026, 1, 1),
    end_date=date(2027, 1, 1),
    expenses=expenses
)

try:
    pdf_path = generate_invoice_pdf(invoice, "test_invoice_25_items.pdf")
    print(f"✅ PDF generated successfully at: {pdf_path}")
    print(f"Total amount: {invoice.total_amount:.2f}")
except Exception as e:
    print(f"❌ Error generating PDF: {e}")
    import traceback
    traceback.print_exc()
