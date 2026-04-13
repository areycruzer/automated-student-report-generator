import matplotlib.pyplot as plt
import seaborn as sns
import os

def generate_charts(student_data: dict, output_dir: str) -> dict:
    """
    Generates 3 charts (Subject Bar, GPA Trend Line, Attendance Pie).
    Returns paths to the saved images.
    """
    sns.set_theme(style="whitegrid")
    os.makedirs(output_dir, exist_ok=True)
    roll_no = student_data.get('Roll_No', 'Unknown')
    paths = {}
    
    # 1. Subject Bar Chart
    subjects = ['Data_Structures', 'Algorithms', 'Operating_Systems', 'Database_Systems', 'Computer_Networks']
    short_subs = ['DS', 'Algo', 'OS', 'DB', 'Net']
    marks = [student_data.get(sub, 0) for sub in subjects]
    
    plt.figure(figsize=(7, 4))
    ax = sns.barplot(x=short_subs, y=marks, hue=short_subs, palette="Blues_d", legend=False)
    ax.set_ylim(0, 100)
    ax.set_title("Current Semester Performance", fontsize=12)
    for i, p in enumerate(ax.patches):
        ax.annotate(f"{marks[i]}", (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha='center', va='center', xytext=(0, 5), textcoords='offset points')
    
    bar_path = os.path.join(output_dir, f"bar_{roll_no}.png")
    plt.tight_layout()
    plt.savefig(bar_path, dpi=150)
    plt.close()
    paths['bar'] = bar_path

    # 2. GPA Trend Line Chart
    semesters = ['Sem 1', 'Sem 2', 'Sem 3', 'Sem 4', 'Sem 5']
    gpas = [
        student_data.get('Sem1_GPA', 0), student_data.get('Sem2_GPA', 0),
        student_data.get('Sem3_GPA', 0), student_data.get('Sem4_GPA', 0),
        student_data.get('Sem5_GPA', 0)
    ]
    plt.figure(figsize=(7, 4))
    sns.lineplot(x=semesters, y=gpas, marker='o', color='crimson', linewidth=2.5, markersize=8)
    plt.ylim(0, 10)
    plt.title("Historical GPA Trend", fontsize=12)
    plt.ylabel("GPA out of 10")
    
    for i, gpa in enumerate(gpas):
        plt.text(i, gpa + 0.3, str(gpa), ha='center', fontsize=9)
        
    line_path = os.path.join(output_dir, f"line_{roll_no}.png")
    plt.tight_layout()
    plt.savefig(line_path, dpi=150)
    plt.close()
    paths['line'] = line_path

    # 3. Attendance Pie Chart
    attended = student_data.get('Attended_Classes', 0)
    total = student_data.get('Total_Classes', 150)
    missed = total - attended
    
    plt.figure(figsize=(5, 5))
    plt.pie([attended, missed], labels=['Attended', 'Missed'], autopct='%1.1f%%', 
            startangle=90, colors=['#2ca02c', '#d62728'], explode=(0.05, 0))
    plt.title("Class Attendance Distribution", fontsize=12)
    
    pie_path = os.path.join(output_dir, f"pie_{roll_no}.png")
    plt.tight_layout()
    plt.savefig(pie_path, dpi=150)
    plt.close()
    paths['pie'] = pie_path

    return paths
