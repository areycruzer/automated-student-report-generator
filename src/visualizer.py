import matplotlib.pyplot as plt
import seaborn as sns
import os

def generate_bar_chart(student_data: dict, output_dir: str) -> str:
    """
    Generates a bar chart for a student's marks and saves it temporarily.
    """
    sns.set_theme(style="whitegrid")
    
    subjects = ['Math', 'Physics', 'Computer_Science']
    marks = [student_data.get(sub, 0) for sub in subjects]
    
    plt.figure(figsize=(6, 4))
    # 'palette' without 'hue' is deprecated, so we use hue=subjects
    ax = sns.barplot(x=subjects, y=marks, hue=subjects, palette="viridis", legend=False)
    ax.set_ylim(0, 100)
    ax.set_ylabel("Marks")
    ax.set_title(f"Academic Performance: {student_data.get('Name', 'Student')}")
    
    # Add values on top of bars
    for i, p in enumerate(ax.patches):
        ax.annotate(f"{marks[i]}", 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha='center', va='center', 
                    xytext=(0, 5), 
                    textcoords='offset points')
                    
    # Ensure output directory exists before saving
    os.makedirs(output_dir, exist_ok=True)
    
    roll_no = student_data.get('Roll_No', 'Unknown')
    chart_path = os.path.join(output_dir, f"chart_{roll_no}.png")
    plt.tight_layout()
    plt.savefig(chart_path)
    plt.close()
    
    return chart_path
