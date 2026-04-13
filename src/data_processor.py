import pandas as pd

def process_student_data(file_path: str) -> pd.DataFrame:
    """
    Reads the CSV, handles missing values, calculates total marks, percentage,
    grade, and class rank.
    """
    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return pd.DataFrame()

    # Handle missing values gracefully by filling them with 0
    subjects = ['Math', 'Physics', 'Computer_Science']
    for sub in subjects:
        if sub in df.columns:
            df[sub] = pd.to_numeric(df[sub], errors='coerce').fillna(0)

    # Calculate Total Marks and Percentage
    df['Total_Marks'] = df[subjects].sum(axis=1)
    df['Percentage'] = (df['Total_Marks'] / 300) * 100

    # Calculate Grade
    def get_grade(percentage):
        if percentage >= 90:
            return 'A'
        elif percentage >= 80:
            return 'B'
        elif percentage >= 70:
            return 'C'
        else:
            return 'F'

    df['Grade'] = df['Percentage'].apply(get_grade)

    # Calculate Class Rank based on Percentage (1 = highest percentage)
    df['Rank'] = df['Percentage'].rank(ascending=False, method='min').astype(int)

    return df
