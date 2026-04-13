# Automated Student Report Generation

A Python-based Command Line Interface (CLI) application that automates the creation of highly detailed, 3-page comprehensive student academic report cards. It reads extended student data from a CSV file, calculates grades and historical statistics, generates multiple performance charts, and compiles everything into professional PDF reports.

## Features
- **Extensive Data Initialization & Processing**: Reads 30+ columns of CSV data including personal demographics, emergency contacts, administrative records, financial status (tuition, fines), and multi-semester historical GPA.
- **Advanced Data Analytics**: Computes Current Semester GPA, specific subject percentages, Letter Grades, Class Ranks, and Attendance percentages using `pandas`. Gracefully handles missing values and data inconsistencies.
- **Multi-Chart Visualizations**: Generates three distinct charts per student using `matplotlib` and `seaborn`:
  - **Bar Chart**: Current semester subject performance assessment.
  - **Line Chart**: Cumulative degree GPA trend across 5 semesters.
  - **Pie Chart**: Class attendance distribution (attended vs. missed).
- **3-Page PDF Generation**: Compiles a professional "University Academic Report" for each student using `fpdf2`.
  - *Page 1*: Personal & Enrollment Information, Contact & Emergency Details, Academic Snapshot.
  - *Page 2*: Detailed Academic Performance table and embedded performance graphics.
  - *Page 3*: Extracurriculars, Campus Life, Attendance (with pie chart), and Administrative/Financial status (with dynamic color-coding for disciplinary actions).
- **CLI Interface**: Simple command-line interface to specify input data and output directories.

## Project Structure

```text
student_report_automation/
├── data/
│   ├── raw_students.csv        # Comprehensive dataset (30+ columns)
│   └── output_reports/         # Directory where generated 3-page PDFs are saved
├── src/
│   ├── __init__.py
│   ├── data_processor.py       # Pandas logic for advanced metrics and ranking
│   ├── visualizer.py           # Matplotlib/Seaborn logic for 3 distinct charts
│   ├── pdf_generator.py        # FPDF layout engine for the 3-page report
│   └── cli.py                  # Argparse CLI setup
├── requirements.txt            # Project dependencies
├── main.py                     # Application entry point
└── README.md                   # Project documentation
```

## Installation

### Prerequisites
- Python 3.7+

### Setup (Linux / macOS / Windows)

It is highly recommended to run this project inside a Python Virtual Environment, especially on modern Linux distributions (like Ubuntu/Debian) to avoid `externally-managed-environment` errors with `pip`.

```bash
# 1. Navigate to the project directory
cd "New Folder"

# 2. Create a virtual environment named 'venv'
python3 -m venv venv

# 3. Activate the virtual environment
# On Linux/macOS:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# 4. Install the required dependencies
pip install -r requirements.txt
```

## Usage

Ensure your virtual environment is active, then run the `main.py` script from the terminal.

```bash
python main.py --input data/raw_students.csv --output data/output_reports/
```

### CLI Arguments
- `--input` (required): Path to the raw CSV file containing the student data.
- `--output` (required): Path to the directory where the PDF reports will be saved.

## Output
Once the script runs successfully, you will find individual PDF report cards inside the specified output directory (e.g., `data/output_reports/Report_101.pdf`). Each PDF contains the student's personal details, extended academic history, multiple graphical charts, and behavioral/administrative status.
