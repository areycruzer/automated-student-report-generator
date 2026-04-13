# Automated Student Report Generation

A Python-based Command Line Interface (CLI) application that automates the creation of professional student academic report cards. It reads student data from a CSV file, calculates grades and statistics, generates per-student performance bar charts, and compiles everything into individual PDF reports.

## Features
- **Data Initialization & Processing**: Reads CSV data and computes Total Marks, Percentage, Letter Grade, and Class Rank using `pandas`. Gracefully handles missing values.
- **Data Visualization**: Generates individual performance bar charts comparing Math, Physics, and Computer Science marks using `matplotlib` and `seaborn`.
- **PDF Generation**: Compiles a professional "University Academic Report" for each student embedding their statistics and generated charts using `fpdf2`.
- **CLI Interface**: Simple command-line interface to specify input data and output directories.

## Project Structure

```text
student_report_automation/
├── data/
│   ├── raw_students.csv        # Sample student data
│   └── output_reports/         # Directory where generated PDFs are saved
├── src/
│   ├── __init__.py
│   ├── data_processor.py       # Pandas logic for grades and ranking
│   ├── visualizer.py           # Matplotlib/Seaborn charting logic
│   ├── pdf_generator.py        # FPDF PDF generation logic
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
Once the script runs successfully, you will find individual PDF report cards inside the specified output directory (e.g., `data/output_reports/Report_101.pdf`). Each PDF contains the student's personal details, academic metrics, and an embedded bar chart of their performance.