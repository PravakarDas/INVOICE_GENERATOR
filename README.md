# 📄 Professional Expense Invoice Generator

A production-ready Flask application for generating professional A4 PDF expense reports with dynamic form management, automatic cleanup, and modern SaaS-style design.

## ✨ Features

- ✅ **Dynamic Expense Management** - Add/remove expense items in real-time
- ✅ **Professional PDF Generation** - A4 portrait PDFs with multi-page support
- ✅ **Modern UI/UX** - Bit Apps Design System with responsive layout
- ✅ **Auto Cleanup** - Automatic PDF cleanup on refresh/navigation
- ✅ **Session Management** - Secure session handling for downloads
- ✅ **Form Validation** - Comprehensive client and server-side validation
- ✅ **Company Logos** - Support for custom company logo watermarks
- ✅ **Production Ready** - Clean architecture, modular design, PEP8 compliant

## 🎨 Design System

Built with the **Bit Apps Professional Design System**:
- **Primary Action**: #2160FD (Royal Blue)
- **Headers**: #0F172A (Midnight Navy)
- **Body Text**: #64748B (Slate Gray)
- **Success**: #10B981
- Modern typography with Inter/Poppins fonts
- Responsive grid layout
- Smooth animations and transitions

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

- Select company from dropdown
- Enter prepared by name
- Enter employee ID
- Enter department
- Select date range (start and end dates)

### 2. Add Expense Items

- Click **"➕ Add Expense Item"** to add rows
- Fill in:
  - **Date** - Date of expense
  - **Category** - Type (Travel, Food, Accommodation, etc.)
  - **Description** - Expense details
  - **Notes** - Optional additional information
  - **Amount** - Cost in dollars
- Click **"×"** button to remove unwanted items
- At least one expense item is required

### 3. Generate PDF

- Click **"📄 Generate Invoice PDF"**
- You'll be redirected to a preview page
- Review invoice details
- Click **"⬇️ Download PDF"** to get your file

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
- Company logo watermark (if available)
- Header with title and date range
- Metadata section with employee info
- Detailed expense table
- Highlighted total amount
- Signature section
- Multi-page support with repeating headers

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

1. Create PNG logo file (recommended: 400x400px)
2. Name it: `company_name.png` (matching form dropdown value)
3. Place in: `static/assets/logos/`
4. Logo will automatically appear in PDFs

## 📦 Dependencies

Main packages:
- **Flask** - Web framework
- **Flask-WTF** - Form handling
- **WTForms** - Form validation
- **ReportLab** - PDF generation

See `requirements.txt` for complete list.

## 🛠️ Development

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

Edit `app/forms.py`:

```python
category = SelectField(
    "Category",
    choices=[
        ("Travel", "Travel"),
        ("YourCategory", "Display Name"),
        # Add more here
    ],
)
```

### Customizing PDF Layout

Edit `app/pdf_generator.py` to modify:
- Page margins
- Table column widths
- Colors and styling
- Header/footer content

## 🚨 Troubleshooting

### Error: "TypeError: 'str' object is not callable"

**Fixed!** This was due to incorrect template field access. Now using `expense.form.field_name`.

### PDFs not generating

1. Check `output/invoices/` directory exists
2. Verify write permissions
3. Check ReportLab installation
4. Review logs for errors

### Logo not appearing

1. Verify logo file exists in `static/assets/logos/`
2. Check filename matches company value
3. Ensure PNG format
4. Check file permissions

### Session issues

1. Clear browser cookies
2. Check SECRET_KEY is set
3. Restart Flask application

## 📝 Production Deployment

For production:

1. **Set SECRET_KEY**:
```python
SECRET_KEY = os.environ.get("SECRET_KEY")
```

2. **Disable Debug Mode**:
```python
app.run(debug=False)
```

3. **Use Production Server**:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 "app:create_app()"
```

4. **Enable HTTPS**:
```python
SESSION_COOKIE_SECURE = True
```

5. **Set up regular cleanup**:
Schedule periodic cleanup of old PDFs via cron or task scheduler.

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
- Check the troubleshooting section
- Review error logs in terminal
- Verify all dependencies are installed

---

**Built with ❤️ using Flask and ReportLab**

*Professional invoice generation made simple.*

