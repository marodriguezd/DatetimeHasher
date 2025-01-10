# Hash Generator

A simple GUI application that generates sequential MD5 hashes based on timestamps with a specified delay between each generation.

## Features

- User-friendly graphical interface
- Generates multiple 8-character MD5 hashes
- Timestamps included with each hash
- Automatic file output saving
- Real-time display in scrollable window

## Requirements

- Python 3.8.x or higher
- tkinter (usually included with Python)
- pyinstaller (for building executable)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/hash-generator.git
cd hash-generator
```

## Usage

Run the Python script:
```bash
python Datetime_to_hash.py
```

Or use the compiled executable:

Enter the desired number of hashes
Click "Generate Hashes"
Results will display in the window and save to ```hashes_output.txt```

## Build Instructions
To create standalone executable:
```bash
pyinstaller --onefile --windowed --name DatetimeHasher Datetime_to_hash.py
```

## Development
This project was developed with the assistance of:

- GitHub Copilot Free:
    - Claude 3.5 Sonnet (Preview)
    - ChatGPT 4o