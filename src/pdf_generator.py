import os
from fpdf import FPDF
from src.visualizer import generate_bar_chart

class PDFReport(FPDF):
    def header(self):
        self.set_font("Helvetica", 'B', 16)
        self.cell(0, 10, "University Academic Report", align='C', new_x="LMARGIN", new_y="NEXT")
        self.ln(10)
        
    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", 'I', 8)
        self.cell(0, 10, f"Page {self.page_no()}", align='C')

def generate_pdf_report(student_data: dict, output_dir: str):
    """
    Generates a professional PDF report card for a single student.
    """
    pdf = PDFReport()
    pdf.add_page()
    
    pdf.set_font("Helvetica", size=12)
    
    # Add Student Details
    details = [
        f"Name: {student_data.get('Name', '')}",
        f"Roll No: {student_data.get('Roll_No', '')}",
        f"Email: {student_data.get('Email', '')}",
        f"Rank: {student_data.get('Rank', '')}",
        f"Total Marks: {student_data.get('Total_Marks', '')} / 300",
        f"Percentage: {student_data.get('Percentage', 0):.2f}%",
        f"Grade: {student_data.get('Grade', '')}"
    ]
    
    for detail in details:
        pdf.cell(0, 8, detail, new_x="LMARGIN", new_y="NEXT")
        
    pdf.ln(10)
    
    # Generate and embed the bar chart
    temp_dir = os.path.join(output_dir, "temp")
    chart_path = generate_bar_chart(student_data, temp_dir)
    
    if os.path.exists(chart_path):
        pdf.image(chart_path, w=120)
        # Clean up temporary chart image
        os.remove(chart_path)
        
    # Ensure output directory exists before saving PDF
    os.makedirs(output_dir, exist_ok=True)
    roll_no = student_data.get('Roll_No', 'Unknown')
    pdf_path = os.path.join(output_dir, f"Report_{roll_no}.pdf")
    pdf.output(pdf_path)
