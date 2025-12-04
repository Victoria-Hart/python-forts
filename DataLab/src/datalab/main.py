"""
Main entry point for DataLab application.

Demonstrates:
- Composing functionality from multiple modules
- Creating a main application flow
- Clean separation between library code and application code
"""

from datalab.utils import log
from datalab.processing import analyze_json_data, analyze_csv_data, print_analysis_report


def run():
    """
    Main application function.

    This is the entry point that orchestrates the entire application.
    It can be called from:
    - CLI: datalab (after pip install)
    - Module: python -m datalab
    - Direct: python main.py (if __name__ == '__main__')
    """
    log("Welcome to DataLab - Data Analysis Tool")
    print()

    # Analyze JSON data
    log("=" * 60)
    json_results = analyze_json_data()
    print_analysis_report(json_results)
    print()

    # Analyze CSV data
    log("=" * 60)
    csv_results = analyze_csv_data()
    print_analysis_report(csv_results)
    print()

    log("=" * 60)
    log("Analysis complete!")


if __name__ == '__main__':
    # This allows the module to be run directly for testing
    run()
