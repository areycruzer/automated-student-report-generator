import os
from src.cli import parse_args
from src.data_processor import process_student_data
from src.pdf_generator import generate_pdf_report

def main():
    args = parse_args()
    
    input_csv = args.input
    output_dir = args.output
    
    print(f"Reading student data from: {input_csv}")
    df = process_student_data(input_csv)
    
    if df.empty:
        print("Failed to process data. Exiting.")
        return
        
    print(f"Successfully processed {len(df)} students. Generating reports...")
    
    # Generate reports for each student
    for _, student in df.iterrows():
        student_data = student.to_dict()
        generate_pdf_report(student_data, output_dir)
        print(f"Generated report for Roll No: {student['Roll_No']}")
        
    print(f"All reports saved to: {output_dir}")

if __name__ == "__main__":
    main()
