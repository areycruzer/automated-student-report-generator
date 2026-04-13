import os
from fpdf import FPDF
from src.visualizer import generate_charts

class PDFReport(FPDF):
    def header(self):
        self.set_font("Helvetica", 'B', 18)
        self.cell(0, 10, "University Academic Report", align='C', new_x="LMARGIN", new_y="NEXT")
        self.set_font("Helvetica", 'I', 10)
        self.cell(0, 6, "Comprehensive Student Profile & Performance Assessment", align='C', new_x="LMARGIN", new_y="NEXT")
        self.line(10, 28, 200, 28)
        self.ln(10)
        
    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", 'I', 8)
        self.cell(0, 10, f"Page {self.page_no()}", align='C')
        
    def section_title(self, title):
        self.set_font("Helvetica", 'B', 14)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 8, title, fill=True, new_x="LMARGIN", new_y="NEXT")
        self.ln(4)

    def kv_row(self, key, value):
        self.set_font("Helvetica", 'B', 11)
        self.cell(50, 8, f"{key}:")
        self.set_font("Helvetica", '', 11)
        self.cell(0, 8, str(value), new_x="LMARGIN", new_y="NEXT")

def generate_pdf_report(student: dict, output_dir: str):
    full_name = f"{student.get('First_Name', '')} {student.get('Last_Name', '')}"
    pdf = PDFReport()
    
    # ================= PAGE 1 =================
    pdf.add_page()
    pdf.section_title("1. Personal & Enrolment Information")
    pdf.kv_row("Full Name", full_name)
    pdf.kv_row("Roll Number", student.get("Roll_No", ""))
    pdf.kv_row("Date of Birth", student.get("DOB", ""))
    pdf.kv_row("Gender", student.get("Gender", ""))
    pdf.kv_row("Blood Group", student.get("Blood_Group", ""))
    pdf.ln(5)
    
    pdf.section_title("2. Contact & Emergency Details")
    pdf.kv_row("Student Email", student.get("Email", ""))
    pdf.kv_row("Student Phone", student.get("Phone", ""))
    pdf.kv_row("Permanent Address", student.get("Address", ""))
    pdf.ln(2)
    pdf.kv_row("Guardian Name", student.get("Guardian_Name", ""))
    pdf.kv_row("Guardian Phone", student.get("Guardian_Phone", ""))
    pdf.ln(10)
    
    pdf.section_title("3. Academic Snapshot")
    pdf.kv_row("Current Program", "B.Tech Computer Science")
    pdf.kv_row("Current Semester", "Semester 5")
    pdf.kv_row("Overall Rank", f"{student.get('Rank', '')} in Class")
    
    # ================= PAGE 2 =================
    pdf.add_page()
    pdf.section_title("4. Detailed Academic Performance")
    pdf.kv_row("Sem 5 Total Marks", f"{student.get('Total_Marks', 0)} / 500")
    pdf.kv_row("Sem 5 Percentage", f"{student.get('Percentage', 0):.2f}%")
    pdf.kv_row("Sem 5 GPA", f"{student.get('Sem5_GPA', 0)} / 10.0")
    pdf.kv_row("Sem 5 Grade", student.get("Sem5_Grade", ""))
    pdf.ln(5)
    
    # Generate Charts
    temp_dir = os.path.join(output_dir, "temp")
    chart_paths = generate_charts(student, temp_dir)
    
    pdf.set_font("Helvetica", 'I', 11)
    pdf.cell(0, 8, "Current Semester Subject Performance:", new_x="LMARGIN", new_y="NEXT")
    if os.path.exists(chart_paths['bar']):
        pdf.image(chart_paths['bar'], w=140)
    
    pdf.ln(5)
    pdf.cell(0, 8, "Cumulative Degree GPA Trend:", new_x="LMARGIN", new_y="NEXT")
    if os.path.exists(chart_paths['line']):
        pdf.image(chart_paths['line'], w=140)

    # ================= PAGE 3 =================
    pdf.add_page()
    pdf.section_title("5. Attendance & Participation")
    pdf.kv_row("Total Classes", student.get("Total_Classes", ""))
    pdf.kv_row("Classes Attended", student.get("Attended_Classes", ""))
    pdf.kv_row("Attendance Pct", f"{student.get('Attendance_Percentage', 0)}%")
    pdf.ln(5)
    
    if os.path.exists(chart_paths['pie']):
        pdf.image(chart_paths['pie'], w=90)
    pdf.ln(5)
    
    pdf.section_title("6. Extracurriculars & Campus Life")
    pdf.kv_row("Club Memberships", student.get("Clubs", "None"))
    pdf.kv_row("Sports Activities", student.get("Sports", "None"))
    pdf.kv_row("Hostel Allocation", f"{student.get('Hostel_Block', '')}, Room {student.get('Room_No', '')}")
    pdf.ln(5)
    
    pdf.section_title("7. Administrative & Financial Status")
    pdf.kv_row("Tuition Paid", student.get("Tuition_Paid", "Unknown"))
    pdf.kv_row("Library Fine Due", f"${student.get('Library_Fine', 0):.2f}")
    
    # Disciplinary coloring check
    disc = str(student.get("Disciplinary_Action", "None"))
    pdf.set_font("Helvetica", 'B', 11)
    pdf.cell(50, 8, "Disciplinary Actions:")
    if disc.lower() == "none" or disc.lower() == "nan":
        pdf.set_text_color(0, 150, 0) # Green
    else:
        pdf.set_text_color(200, 0, 0) # Red
    pdf.cell(0, 8, disc, new_x="LMARGIN", new_y="NEXT")
    pdf.set_text_color(0, 0, 0) # Reset
    
    # Save & Cleanup
    os.makedirs(output_dir, exist_ok=True)
    pdf_path = os.path.join(output_dir, f"Report_{student.get('Roll_No', 'Unknown')}.pdf")
    pdf.output(pdf_path)
    
    # Clean up charts
    for path in chart_paths.values():
        if os.path.exists(path):
            os.remove(path)
