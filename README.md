# 📄 Professional Expense Invoice Generator

A production-ready Flask application for generating professional A4 PDF expense reports with dynamic form management, automatic cleanup, and modern SaaS-style design. Designed for **Bangladesh-based companies** with **BDT currency support**.

## ✨ Features

- ✅ **Dynamic Expense Management** - Add/remove expense items in real-time
- ✅ **Professional PDF Generation** - A4 portrait PDFs with multi-page support and company logo watermarks
- ✅ **Modern UI/UX** - Bit Apps Design System with responsive layout
- ✅ **Auto Cleanup** - Automatic PDF cleanup on refresh/navigation (1 hour expiry)
- ✅ **Session Management** - Secure session handling for downloads
- ✅ **Form Validation** - Comprehensive client and server-side validation with date range controls
- ✅ **Company Logos** - Support for BitApps and BitCode company logo watermarks
- ✅ **Production Ready** - Clean architecture, modular design, PEP8 compliant
- ✅ **Custom Naming** - Intelligent PDF naming: `startdate_enddate_preparedby_company.pdf`
- ✅ **BDT Currency** - All amounts in Bangladeshi Taka

## 🎨 Design System

Built with the **Bit Apps Professional Design System**:
- **Primary Blue**: #2563EB - Action buttons and totals
- **Header Navy**: #1E3A8A - Document headers and titles
- **Text Dark**: #1F2937 - Primary text content
- **Text Light**: #6B7280 - Secondary text and labels
- **Border Gray**: #E5E7EB - Table borders and dividers
- **Success Green**: #10B981 - Success messages
- Modern typography with Helvetica font family
- Responsive grid layout
- Smooth animations and transitions
- Logo watermark at 10% opacity for professional branding

## 📁 Project Structure

```
invoice_generator/
│
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── routes.py            # Route handlers & controllers
│   ├── forms.py             # WTForms definitions
│   ├── pdf_generator.py     # ReportLab PDF generation
│   ├── models.py            # Data models
│   └── utils.py             # Utility functions & cleanup
│
├── templates/
│   ├── base.html            # Base template layout
│   ├── invoice_form.html    # Main form with dynamic items
│   └── invoice_preview.html # Download preview page
│
├── static/
│   ├── css/
│   │   └── style.css        # Professional styling
│   └── assets/
│       └── logos/           # Company logo files
│           ├── company1.png
│           └── company2.png
│
├── output/
│   └── invoices/            # Generated PDFs (auto-cleanup)
│
├── config.py                # Configuration settings
├── run.py                   # Application entry point
├── test_form.py             # Sample test data (25 expense items)
├── gunicorn_config.py       # Gunicorn WSGI server config
├── render.yaml              # Render deployment configuration
├── requirements.txt         # Python dependencies
└── README.md                # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Installation

1. **Clone or download the project**

```bash
cd invoice_generator
```

2. **Create and activate virtual environment**

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the application**

```bash
python run.py
```

5. **Open in browser**

Navigate to: `http://127.0.0.1:5000`

## 📖 How to Use

### 1. Fill Company Information

- **Company**: Select from dropdown (BitApps or BitCode)
- **Prepared By**: Enter employee name
- **Employee ID**: Enter employee identifier
- **Department**: Select department (Private or HR)
- **Start Date**: Select period start date
- **End Date**: Select period end date (must be after start date)

> **Note**: Expense dates will be automatically limited to the selected date range.

### 2. Add Expense Items

- Click **"➕ Add Expense Item"** to add rows
- Fill in:
  - **Date** - Date of expense (within start/end date range)
  - **Category** - Select from dropdown:
    - Transportation
    - Electricity bill
    - Sports
    - Stationary
    - Snacks
    - Electronic item
    - Servicing
    - Tax (TDS/VDS)
    - Internet Bill
    - Expense from employee
    - Ama Tea Coffee
    - Mobile Recharge
    - Trade License
    - Others
    - Others bill
    - Rent
    - PiHR
    - Courier Service
    - Office Equipment
  - **Description** - Expense details (required)
  - **Notes** - Optional additional information
  - **Amount** - Cost in **BDT** (Bangladeshi Taka, minimum 0.01)
- Click **"×"** button to remove unwanted items
- At least one expense item is required

### 3. Generate PDF

- Click **"📄 Generate Invoice PDF"**
- You'll be redirected to a preview page showing:
  - Company name
  - Prepared by name
  - Date range
  - Total amount in BDT
- Click **"⬇️ Download PDF"** to get your file
- PDF filename format: `MMDDYYYY_MMDDYYYY_PreparedBy_Company.pdf`
  - Example: `01052026_01012027_JohnDoe_BitApps.pdf`

### 4. Create New Invoice

- Click **"➕ Create New Invoice"** to start over
- Previous PDF is automatically cleaned up
- Session data is cleared

## 🎯 Key Features Explained

### Dynamic Item Management

JavaScript-powered dynamic rows allow users to:
- Add unlimited expense items
- Remove items (minimum 1 required)
- Auto-reindexing of form fields
- Smooth scrolling to new items

### Auto Cleanup System

The application automatically:
- Deletes PDFs older than 1 hour
- Removes session invoice on page refresh
- Cleans up on navigation back to form
- Prevents disk space accumulation

### PDF Design

Professional invoices include:
- **Top blue line** - Brand accent color (#2563EB)
- **Company name header** - Company identification
- **Expense Report title** - Bold navy header (#1E3A8A)
- **Date range subtitle** - Period covered by the report
- **Metadata section** - 3-column layout with:
  - Prepared By
  - Employee ID
  - Department
- **Expense table** - Professional grid with columns:
  - Date (DD-Mon-YYYY format)
  - Category
  - Description
  - Notes
  - Amount (BDT X,XXX.XX format, right-aligned)
- **Total amount** - Large blue text highlighting total in BDT
- **Signature section** - Space for manual signature and date
- **Company logo watermark** - Centered, semi-transparent (10% opacity)
- **Multi-page support** - Table headers repeat on each page
- **Professional spacing** - 20mm margins with optimized layout

### Security Features

- CSRF protection on all forms
- Session-based file access control
- Secure cookie configuration
- Input validation and sanitization

## 🔧 Configuration

Edit `config.py` to customize:

```python
SECRET_KEY = "your-secret-key-here"  # Change in production!
CLEANUP_MAX_AGE = 3600  # PDF cleanup age (seconds)
PERMANENT_SESSION_LIFETIME = 3600  # Session duration
```

### Adding Company Logos

1. Create PNG logo file (recommended: square aspect ratio, e.g., 400x400px)
2. Name it exactly as company name: `BitApps.png` or `BitCode.png`
3. Place in: `static/assets/logos/`
4. Logo will automatically appear as watermark in PDFs (centered, 10% opacity)

**Current supported companies:**
- BitApps
- BitCode

To add new companies:
1. Edit `app/forms.py` - add to `company` SelectField choices
2. Add corresponding logo file to `static/assets/logos/`

## 📦 Dependencies

Main packages:
- **Flask 3.0.0** - Web framework
- **Flask-WTF 1.2.1** - Form handling with CSRF protection
- **WTForms 3.1.2** - Form validation
- **ReportLab 4.0.9** - Professional PDF generation
- **Pillow ≥10.0.0** - Image processing for logo watermarks

See `requirements.txt` for complete list.

## 🛠️ Development

### Testing with Sample Data

A test file is included with sample data:

```bash
python test_form.py
```

This generates a sample invoice with:
- 25 expense items
- Date range: 01/01/2026 - 01/01/2027
- Company: BitApps
- Various expense categories
- Total: ~BDT 773,200.00

### Code Style

- Follow PEP8 guidelines
- Use type hints where appropriate
- Add docstrings to functions/classes
- Keep functions focused and modular

### Testing

Run the development server:
```bash
python run.py
```

The app runs in debug mode by default with auto-reload.

### Adding Categories

Edit `app/forms.py` in the `ExpenseForm` class:

```python
category = SelectField(
    "Category",
    choices=[
        ("Transportation", "Transportation"),
        ("YourNewCategory", "Your New Category"),
        # Add more categories here
    ],
    validators=[DataRequired()],
)
```

**Current categories include:**
- Transportation, Electricity bill, Sports, Stationary
- Snacks, Electronic item, Servicing, Tax (TDS/VDS)
- Internet Bill, Expense from employee, Ama Tea Coffee
- Mobile Recharge, Trade License, Rent, PiHR
- Courier Service, Office Equipment, Others, Others bill

### Adding Departments

Edit `app/forms.py` in the `InvoiceForm` class:

```python
department = SelectField(
    "Department",
    choices=[
        ("Private", "Private"),
        ("HR", "HR"),
        ("YourDepartment", "Your Department"),
        # Add more departments here
    ],
    validators=[DataRequired()],
)
```

### Customizing PDF Layout

Edit `app/pdf_generator.py` to modify:
- **Page margins**: Currently 20mm left/right, 15mm top/bottom
- **Table column widths**: Date (28mm), Category (28mm), Description (52mm), Notes (40mm), Amount (22mm)
- **Colors**: 
  - PRIMARY_BLUE = #2563EB
  - HEADER_NAVY = #1E3A8A
  - TEXT_DARK = #1F2937
  - TEXT_LIGHT = #6B7280
  - BORDER_GRAY = #E5E7EB
- **Watermark opacity**: Currently 0.1 (10%)
- **Watermark size**: Currently 200x200 pixels
- **Font sizes**: Title (18pt), Headers (10pt), Table (9pt), Total (14pt)
- **Currency format**: BDT X,XXX.XX (comma-separated thousands)
- **Date format**: DD-Mon-YYYY (e.g., 05-Jan-2026)

### PDF Filename Customization

The PDF naming format is defined in `app/routes.py`:
```python
# Format: MMDDYYYY_MMDDYYYY_PreparedBy_Company.pdf
start_str = invoice.start_date.strftime('%m%d%Y')
end_str = invoice.end_date.strftime('%m%d%Y')
prepared_by_clean = invoice.prepared_by.replace(' ', '')
company_clean = invoice.company.replace(' ', '')
filename = f"{start_str}_{end_str}_{prepared_by_clean}_{company_clean}.pdf"
```

## 🚨 Troubleshooting

### Error: "Module not found" or "ImportError"

**Solution**: Make sure virtual environment is activated and dependencies are installed:
```bash
# Activate venv
.\venv\Scripts\Activate.ps1  # Windows
source venv/bin/activate      # macOS/Linux

# Install dependencies
pip install -r requirements.txt
```

### PDFs not generating

1. Check `output/invoices/` directory exists (created automatically)
2. Verify write permissions on the directory
3. Check ReportLab and Pillow are installed: `pip list | grep -i reportlab`
4. Review terminal logs for error messages
5. Ensure at least one expense item is added

### Logo not appearing as watermark

1. Verify logo file exists in `static/assets/logos/`
2. Check filename **exactly** matches company name (e.g., `BitApps.png`, not `bitapps.png`)
3. Ensure PNG format with transparent background for best results
4. Check file permissions (readable)
5. Watermark is intentionally subtle (10% opacity) - check carefully

### Session issues / "Invalid download request"

1. Clear browser cookies and cache
2. Check `SECRET_KEY` is set in `config.py`
3. Restart Flask application
4. Don't share download links - they're session-specific
5. PDF links expire when you navigate back or refresh

### Date validation errors

- End date must be **after or equal to** start date
- Expense dates must fall **within** the start/end date range
- Use proper date format: MM/DD/YYYY

### Form validation fails / "Please add at least one expense item"

- Ensure at least ONE expense row exists
- All required fields must be filled:
  - Date, Category, Description, Amount
  - Note field is optional
- Amount must be greater than 0.01

## 📝 Production Deployment

### Quick Deploy to Render (Recommended)

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com)

**Automatic Deployment:**

1. **Push to GitHub** (if not already done)
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/yourusername/invoice-generator.git
   git push -u origin main
   ```

2. **Create New Web Service on Render**
   - Go to [Render Dashboard](https://dashboard.render.com/)
   - Click **"New +"** → **"Web Service"**
   - Connect your GitHub repository
   - Render will auto-detect `render.yaml` configuration

3. **Configure (Auto-detected from render.yaml)**
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn -c gunicorn_config.py "app:create_app()"`
   - **Environment Variables**: Auto-generated SECRET_KEY

4. **Deploy**
   - Click **"Create Web Service"**
   - Render will build and deploy automatically
   - Your app will be live at `https://your-app-name.onrender.com`

**Manual Configuration (if render.yaml not detected):**

1. **Environment**: Python 3
2. **Build Command**: `pip install -r requirements.txt`
3. **Start Command**: `gunicorn -c gunicorn_config.py "app:create_app()"`
4. **Add Environment Variable**:
   - `SECRET_KEY`: Generate with `python -c "import secrets; print(secrets.token_hex(32))"`
   - `FLASK_ENV`: `production`

**Important Notes for Render:**
- ✅ App now binds to `0.0.0.0` (required by Render)
- ✅ Uses `PORT` environment variable from Render
- ✅ Gunicorn WSGI server included
- ✅ Auto-deploy on git push enabled
- ⚠️ Free tier may have cold starts (15-30 seconds)
- ⚠️ PDFs stored temporarily (ephemeral filesystem on free tier)

---

### General Production Deployment

For production deployment on any platform:

### 1. Environment Variables

Set secure `SECRET_KEY`:
```python
# config.py
SECRET_KEY = os.environ.get("SECRET_KEY")  # Set via environment variable
```

Generate secure key:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

### 2. Disable Debug Mode

Edit `run.py`:
```python
if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=8000)
```

### 3. Use Production WSGI Server

Install and run with Gunicorn:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 "app:create_app()"
```

Or with uWSGI:
```bash
pip install uwsgi
uwsgi --http :8000 --wsgi-file run.py --callable app --processes 4 --threads 2
```

### 4. Enable HTTPS (Recommended)

Edit `config.py`:
```python
SESSION_COOKIE_SECURE = True  # Only send cookies over HTTPS
SESSION_COOKIE_HTTPONLY = True  # Prevent XSS attacks
SESSION_COOKIE_SAMESITE = 'Lax'  # CSRF protection
```

### 5. Automated PDF Cleanup

Set up scheduled cleanup of old PDFs:

**Windows Task Scheduler**: Run daily cleanup script
**Linux Cron**: 
```bash
# Run cleanup every hour
0 * * * * /path/to/venv/bin/python /path/to/cleanup_script.py
```

Or adjust `CLEANUP_MAX_AGE` in `config.py` (default: 3600 seconds / 1 hour)

### 6. Database (Optional Future Enhancement)

Current implementation uses session-based storage. For multi-user production:
- Consider adding SQLite/PostgreSQL for invoice history
- Implement user authentication
- Add invoice search and archive features

### 7. Reverse Proxy (Nginx/Apache)

Example Nginx configuration:
```nginx
server {
    listen 80;
    server_name yourdomain.com;
    
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
    
    location /static {
        alias /path/to/invoice_generator/static;
    }
}
```

## 📄 License

This project is provided as-is for educational and commercial use.

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 💡 Support

For issues or questions:
- Check the **Troubleshooting** section above
- Review error logs in terminal/console
- Verify all dependencies are installed correctly
- Ensure virtual environment is activated
- Check file permissions for `output/invoices/` directory

## 🎓 Technical Architecture

### Application Flow

1. **User Access** → Flask routes (`app/routes.py`)
2. **Form Rendering** → WTForms validation (`app/forms.py`)
3. **Data Validation** → Server-side + client-side JavaScript
4. **Data Modeling** → Dataclasses (`app/models.py`)
5. **PDF Generation** → ReportLab (`app/pdf_generator.py`)
6. **File Storage** → `output/invoices/` directory
7. **Session Management** → Flask sessions with cleanup (`app/utils.py`)
8. **Download** → Secure session-based file serving

### Security Features Implemented

- ✅ **CSRF Protection**: WTForms CSRF tokens on all forms
- ✅ **Session Security**: HTTPOnly, SameSite cookies
- ✅ **Input Validation**: Server-side validation with WTForms
- ✅ **Secure Downloads**: Session-based file access control
- ✅ **Auto Cleanup**: Prevents disk space attacks
- ✅ **Safe File Naming**: Sanitized filenames (spaces removed)

### Performance Optimizations

- Automatic cleanup of old PDFs (prevents disk bloat)
- Session-based temporary storage
- Efficient ReportLab table generation
- Minimal dependencies (lightweight stack)
- Static file caching via Flask

## 🚀 Future Enhancements (Roadmap)

Potential features for future versions:

- [ ] User authentication and multi-user support
- [ ] Database integration for invoice history
- [ ] Export to Excel/CSV formats
- [ ] Email invoice delivery
- [ ] Invoice templates selection
- [ ] Dark mode UI
- [ ] API endpoints for programmatic access
- [ ] Invoice search and filtering
- [ ] Bulk invoice generation
- [ ] Custom branding per company
- [ ] Multi-currency support
- [ ] Expense receipt attachments

## 👨‍💻 Credits

**Created and maintained by**: [Pravakar Das](https://pdfolio-rho.vercel.app/)

Built with modern Flask best practices and professional PDF generation techniques.

---

**Built with ❤️ using Flask, ReportLab, and WTForms**

*Professional expense invoice generation for Bangladesh-based companies - Simple, Secure, and Efficient.*

