import pandas as pd

def process_student_data(file_path: str) -> pd.DataFrame:
    """
    Reads the CSV, handles missing values, calculates total marks, percentage,
    Current Sem GPA, attendance percentage, and class rank.
    """
    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return pd.DataFrame()

    # Subjects for Current Semester (Sem 5)
    subjects = ['Data_Structures', 'Algorithms', 'Operating_Systems', 'Database_Systems', 'Computer_Networks']
    
    # Handle missing values gracefully
    for sub in subjects:
        if sub in df.columns:
            df[sub] = pd.to_numeric(df[sub], errors='coerce').fillna(0)

    # Calculate Total Marks and Percentage (Out of 500)
    df['Total_Marks'] = df[subjects].sum(axis=1)
    df['Percentage'] = (df['Total_Marks'] / (len(subjects) * 100)) * 100

    # Calculate Current Semester GPA (Assuming 10-point scale based on percentage)
    df['Sem5_GPA'] = (df['Percentage'] / 10).round(2)

    # Calculate overall Grade based on Sem 5 Percentage
    def get_grade(percentage):
        if percentage >= 90: return 'A+'
        elif percentage >= 80: return 'A'
        elif percentage >= 70: return 'B'
        elif percentage >= 60: return 'C'
        else: return 'F'

    df['Sem5_Grade'] = df['Percentage'].apply(get_grade)

    # Attendance
    df['Total_Classes'] = pd.to_numeric(df['Total_Classes'], errors='coerce').fillna(150)
    df['Attended_Classes'] = pd.to_numeric(df['Attended_Classes'], errors='coerce').fillna(0)
    df['Attendance_Percentage'] = ((df['Attended_Classes'] / df['Total_Classes']) * 100).round(2)

    # Class Rank
    df['Rank'] = df['Percentage'].rank(ascending=False, method='min').astype(int)

    return df
