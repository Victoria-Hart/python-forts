# DataLab - Data Analysis Laboratory

A pedagogical Python package for the Python Advanced course, demonstrating best practices in module management and package structure.

## Installation

```bash
# Install in development mode (editable)
pip install -e .

# Or install normally
pip install .
```

## Usage

### As a CLI tool
After installation, run from anywhere:
```bash
datalab
```

### As a Python module
```bash
python -m datalab
```

### As a library
```python
from datalab import analyze_csv_data, log

results = analyze_csv_data()
log(f"Found {results['records']} records")
```

## Project Structure

```
DataLab/                      # PROJECT ROOT
├── .venv/                    # Virtual environment (create with: python -m venv .venv)
├── requirements.txt          # Dependencies
├── pyproject.toml            # Package configuration
├── README.md                 # This file
├── CODE_GUIDE.md             # Detailed code guide for teaching
└── src/                      # Source directory (src layout)
    └── datalab/              # Main package
        ├── __init__.py       # Package API
        ├── __main__.py       # Module entry point
        ├── config.py         # Configuration & paths
        ├── main.py           # Application entry point
        ├── processing.py     # Data processing
        ├── statistics.py     # Statistical functions
        ├── module_io.py      # I/O operations
        ├── utils.py          # Utilities
        └── data/             # Data files
            ├── data.json
            └── people.csv
```

## Key Concepts Demonstrated

- **Absolute imports**: All imports use full package paths
- **Path handling**: Using `__file__` and `pathlib` for robust paths
- **Configuration**: Centralized in `config.py`
- **Package structure**: Proper use of `__init__.py`
- **Multiple entry points**: CLI, module, and library usage
- **Module testing**: All modules can be tested individually
