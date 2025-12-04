"""
Utility functions for DataLab.

Demonstrates:
- Importing from config module
- Simple utility functions
- Module-level testing with if __name__ == '__main__'
"""

from datalab import config


def log(msg):
    """
    Print a formatted log message.

    Uses the LOG_PREFIX from config module, demonstrating
    centralized configuration.
    """
    print(f'{config.LOG_PREFIX} {msg}')


def format_number(number, decimals=None):
    """
    Format a number with specified decimal places.

    Args:
        number: Number to format
        decimals: Number of decimal places (uses config default if None)

    Returns:
        Formatted string
    """
    if decimals is None:
        decimals = config.DECIMAL_PLACES
    return f'{number:.{decimals}f}'
