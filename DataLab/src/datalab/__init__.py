"""
DataLab - Data Analysis Laboratory
===================================

Basic Usage:
    >>> from datalab import analyze_csv_data, analyze_json_data
    >>> results = analyze_csv_data()
    >>> print(results)

Modules:
    - config: Configuration and path management
    - utils: Utility functions (logging, formatting)
    - module_io: File I/O operations (JSON, CSV)
    - statistics: Statistical analysis functions
    - processing: High-level data processing
    - main: Application entry point
"""

# Package metadata
__version__ = '0.1.0'

# Import key functions for easy access
# This allows users to do: from datalab import log, analyze_csv_data
# instead of: from datalab.utils import log; from datalab.processing import analyze_csv_data
from datalab.utils import log, format_number
from datalab.processing import analyze_json_data, analyze_csv_data, print_analysis_report
from datalab.module_io import load_json, save_json, load_csv, save_csv
from datalab.statistics import calculate_average, calculate_sum, count_by_field
from datalab import config

# Define what gets exported with "from datalab import *"
# (Though explicit imports are preferred!)
__all__ = [
    # Utils
    'log',
    'format_number',
    # Processing
    'analyze_json_data',
    'analyze_csv_data',
    'print_analysis_report',
    # I/O
    'load_json',
    'save_json',
    'load_csv',
    'save_csv',
    # Statistics
    'calculate_average',
    'calculate_sum',
    'count_by_field',
    # Config
    'config',
]
