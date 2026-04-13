import argparse

def parse_args():
    """
    Parses command-line arguments for the report generator.
    """
    parser = argparse.ArgumentParser(description="Automated Student Report Generation")
    
    parser.add_argument(
        "--input", 
        type=str, 
        required=True, 
        help="Path to the raw CSV file containing student data"
    )
    
    parser.add_argument(
        "--output", 
        type=str, 
        required=True, 
        help="Path to the directory where PDF reports will be saved"
    )
    
    return parser.parse_args()
