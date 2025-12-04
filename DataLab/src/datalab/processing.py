"""
Data processing functions for DataLab.

Demonstrates:
- Absolute imports from multiple modules
- Using centralized config
- Composing functions from other modules
- Working with different data formats
"""

from datalab import config
from datalab.module_io import load_json, load_csv
from datalab.statistics import calculate_average, count_by_field, get_min_max
from datalab.utils import log, format_number


def analyze_json_data(filename=None):
    """
    Load and analyze JSON data.

    Args:
        filename: JSON filename (uses default if None)

    Returns:
        Dictionary with analysis results
    """
    if filename is None:
        filename = config.DEFAULT_JSON_FILE

    filepath = config.get_data_path(filename)
    data = load_json(filepath)

    avg_age = calculate_average(data, 'age')

    return {
        'file': filename,
        'records': len(data),
        'average_age': avg_age,
    }


def analyze_csv_data(filename=None):
    """
    Load and analyze CSV data.

    Demonstrates working with CSV files and performing
    multiple statistical analyses.

    Args:
        filename: CSV filename (uses default if None)

    Returns:
        Dictionary with analysis results
    """
    if filename is None:
        filename = config.DEFAULT_CSV_FILE

    filepath = config.get_data_path(filename)
    data = load_csv(filepath)

    # Perform various analyses
    avg_age = calculate_average(data, 'age')
    avg_salary = calculate_average(data, 'salary')
    city_distribution = count_by_field(data, 'city')
    min_salary, max_salary = get_min_max(data, 'salary')

    return {
        'file': filename,
        'records': len(data),
        'average_age': avg_age,
        'average_salary': avg_salary,
        'city_distribution': city_distribution,
        'salary_range': (min_salary, max_salary),
    }


def print_analysis_report(analysis):
    """
    Print a formatted analysis report.

    Args:
        analysis: Dictionary with analysis results
    """
    log(f"Analysis of {analysis['file']}")
    log(f"Total records: {analysis['records']}")
    log(f"Average age: {format_number(analysis['average_age'])}")

    if 'average_salary' in analysis:
        log(f"Average salary: {format_number(analysis['average_salary'], 0)} SEK")
        min_sal, max_sal = analysis['salary_range']
        log(f"Salary range: {format_number(min_sal, 0)} - {format_number(max_sal, 0)} SEK")

    if 'city_distribution' in analysis:
        log("City distribution:")
        for city, count in analysis['city_distribution'].items():
            log(f"  {city}: {count}")
