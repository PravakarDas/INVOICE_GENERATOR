"""
PDF generation module for professional expense invoices.
Uses ReportLab to create A4 portrait PDFs with Bit Apps design system.
Matches Bangladesh-based company design with BDT currency.
"""

import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_RIGHT, TA_LEFT
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Table,
    TableStyle,
    Spacer,
    Image,
    PageBreak,
)
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from config import Config


# Bit Apps Design System Colors (matching the provided design)
PRIMARY_BLUE = HexColor("#2563EB")  # Blue color from the image
HEADER_NAVY = HexColor("#1E3A8A")   # Dark navy for headers
TEXT_DARK = HexColor("#1F2937")     # Dark gray for text
TEXT_LIGHT = HexColor("#6B7280")    # Light gray for secondary text
BORDER_GRAY = HexColor("#E5E7EB")   # Light gray for borders
TOTAL_BLUE = HexColor("#2563EB")    # Blue for total amount


class NumberedCanvas(canvas.Canvas):
    """Custom canvas to add watermark on every page."""
    
    def __init__(self, *args, **kwargs):
        self.logo_path = kwargs.pop('logo_path', None)
        canvas.Canvas.__init__(self, *args, **kwargs)
        
    def showPage(self):
        """Override to add watermark before showing page."""
        self.add_watermark()
        canvas.Canvas.showPage(self)
        
    def add_watermark(self):
        """Add centered logo watermark on the page."""
        if self.logo_path and os.path.exists(self.logo_path):
            try:
                # Save the state
                self.saveState()
                
                # Set transparency for watermark
                self.setFillAlpha(0.1)
                
                # Calculate center position
                page_width, page_height = A4
                logo_size = 200  # Size of watermark logo
                x = (page_width - logo_size) / 2
                y = (page_height - logo_size) / 2
                
                # Draw the watermark image
                self.drawImage(
                    self.logo_path,
                    x, y,
                    width=logo_size,
                    height=logo_size,
                    preserveAspectRatio=True,
                    mask='auto'
                )
                
                # Restore the state
                self.restoreState()
            except Exception as e:
                pass  # Silently fail if watermark can't be added


def generate_invoice_pdf(invoice, filename: str) -> str:
    """
    Generate a professional A4 PDF invoice matching Bangladesh design.
    
    Args:
        invoice: Invoice object containing all expense data
        filename: Output PDF filename
        
    Returns:
        str: Full path to generated PDF file
    """
    output_path = os.path.join(Config.OUTPUT_DIR, filename)

    # Ensure output directory exists
    os.makedirs(Config.OUTPUT_DIR, exist_ok=True)
    
    # Get logo path for watermark
    logo_path = os.path.join(
        Config.BASE_DIR,
        "static",
        "assets",
        "logos",
        f"{invoice.company}.png",
    )
    
    # Create PDF document with custom canvas for watermark
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        rightMargin=20 * mm,
        leftMargin=20 * mm,
        topMargin=15 * mm,
        bottomMargin=15 * mm,
    )

    # Build styles
    styles = getSampleStyleSheet()
    story = []
    
    # ===== TOP BLUE LINE =====
    top_line_data = [[""]]
    top_line = Table(top_line_data, colWidths=[170 * mm], rowHeights=[3])
    top_line.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), PRIMARY_BLUE),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
    ]))
    story.append(top_line)
    story.append(Spacer(1, 8))
    
    # ===== COMPANY NAME =====
    company_style = ParagraphStyle(
        'CompanyName',
        parent=styles['Normal'],
        fontSize=10,
        textColor=TEXT_DARK,
        fontName='Helvetica',
        alignment=TA_LEFT,
    )
    story.append(Paragraph(f"<b>{invoice.company}</b>", company_style))

    story.append(Spacer(1, 10))
    
    # ===== HORIZONTAL LINE =====
    line_data = [[""]]
    line = Table(line_data, colWidths=[170 * mm], rowHeights=[0.5])
    line.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), BORDER_GRAY),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
    ]))
    story.append(line)
    story.append(Spacer(1, 15))
    
    # ===== TITLE =====
    title_style = ParagraphStyle(
        'Title',
        parent=styles['Heading1'],
        fontSize=18,
        textColor=HEADER_NAVY,
        fontName='Helvetica-Bold',
        alignment=TA_LEFT,
        spaceAfter=6,
    )
    story.append(Paragraph("Expense Report", title_style))
    
    # ===== DATE RANGE =====
    date_style = ParagraphStyle(
        'DateRange',
        parent=styles['Normal'],
        fontSize=9,
        textColor=TEXT_LIGHT,
        fontName='Helvetica',
        alignment=TA_LEFT,
        spaceAfter=15,
    )
    date_range = f"{invoice.start_date.strftime('%d/%m/%Y')} – {invoice.end_date.strftime('%d/%m/%Y')}"
    story.append(Paragraph(date_range, date_style))
    story.append(Spacer(1, 10))
    
    # ===== METADATA (3 COLUMNS) =====
    meta_style = ParagraphStyle(
        'MetaInfo',
        parent=styles['Normal'],
        fontSize=9,
        textColor=TEXT_DARK,
        fontName='Helvetica',
        alignment=TA_LEFT,
        leading=14,
    )
    
    meta_data = [[
        Paragraph(f"<b>Prepared By:</b><br/>{invoice.prepared_by}", meta_style),
        Paragraph(f"<b>Employee ID:</b><br/>{invoice.employee_id}", meta_style),
        Paragraph(f"<b>Department:</b><br/>{invoice.department}", meta_style),
    ]]
    
    meta_table = Table(meta_data, colWidths=[56 * mm, 56 * mm, 56 * mm])
    meta_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 20))
    
    # ===== EXPENSE TABLE =====
    table_header_style = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontSize=9,
        textColor=TEXT_DARK,
        fontName='Helvetica-Bold',
        alignment=TA_LEFT,
    )
    
    table_cell_style = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontSize=9,
        textColor=TEXT_DARK,
        fontName='Helvetica',
        alignment=TA_LEFT,
    )
    
    # Build table data
    table_data = [
        [
            Paragraph("<b>Date</b>", table_header_style),
            Paragraph("<b>Category</b>", table_header_style),
            Paragraph("<b>Description</b>", table_header_style),
            Paragraph("<b>Notes</b>", table_header_style),
            Paragraph("<b>Amount</b>", table_header_style),
        ]
    ]
    
    # Add expense items
    for item in invoice.expenses:
        table_data.append([
            Paragraph(item.date.strftime("%d-%b-%Y"), table_cell_style),
            Paragraph(item.category, table_cell_style),
            Paragraph(item.description, table_cell_style),
            Paragraph(item.note or "", table_cell_style),
            Paragraph(f"BDT {item.amount:,.2f}", table_cell_style),
        ])
    
    # Create the table
    expense_table = Table(
        table_data,
        colWidths=[28 * mm, 28 * mm, 52 * mm, 40 * mm, 22 * mm],
        repeatRows=1,
    )
    
    expense_table.setStyle(TableStyle([
        # Header row
        ('BACKGROUND', (0, 0), (-1, 0), HexColor("#F9FAFB")),
        ('TEXTCOLOR', (0, 0), (-1, 0), TEXT_DARK),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('TOPPADDING', (0, 0), (-1, 0), 8),
        ('LINEBELOW', (0, 0), (-1, 0), 1, BORDER_GRAY),
        
        # Data rows
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('TOPPADDING', (0, 1), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        
        # Amount column right-aligned
        ('ALIGN', (4, 1), (4, -1), 'RIGHT'),
        
        # Grid lines
        ('LINEBELOW', (0, 1), (-1, -1), 0.5, BORDER_GRAY),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    
    story.append(expense_table)
    story.append(Spacer(1, 20))
    
    # ===== TOTAL AMOUNT =====
    total_style = ParagraphStyle(
        'TotalAmount',
        parent=styles['Normal'],
        fontSize=14,
        textColor=TOTAL_BLUE,
        fontName='Helvetica-Bold',
        alignment=TA_RIGHT,
    )
    
    total_text = f"BDT {invoice.total_amount:,.2f}"
    story.append(Paragraph(total_text, total_style))
    story.append(Spacer(1, 40))
    
    # ===== SIGNATURE SECTION =====
    sig_style = ParagraphStyle(
        'Signature',
        parent=styles['Normal'],
        fontSize=9,
        textColor=TEXT_DARK,
        fontName='Helvetica',
        alignment=TA_LEFT,
    )
    
    signature_data = [[
        Paragraph("<b>Signature:</b>", sig_style),
        Paragraph("<b>Date:</b>", sig_style),
    ]]
    
    signature_table = Table(signature_data, colWidths=[85 * mm, 85 * mm])
    signature_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
    ]))
    
    story.append(signature_table)
    
    # Build the PDF with watermark canvas
    if logo_path and os.path.exists(logo_path):
        doc.build(story, canvasmaker=lambda *args, **kwargs: NumberedCanvas(*args, logo_path=logo_path, **kwargs))
    else:
        doc.build(story)
    
    return output_path

