# Hash Generator

A simple GUI application that generates sequential MD5 hashes based on timestamps with a specified delay between each generation.

![App Image](https://i.imgur.com/u4frjdZ.png)

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

These AI tools were used for code generation, optimization, and documentation purposes.

## Sample Output
```bash
Generating 3 hashes with 0.1s delay between each:
Hash 1: a1b2c3d4 (Time: 2024-03-21 10:15:30.123456)
Hash 2: e5f6g7h8 (Time: 2024-03-21 10:15:30.223456)
Hash 3: i9j0k1l2 (Time: 2024-03-21 10:15:30.323456)
```

## License

Apache License 2.0

Copyright 2024