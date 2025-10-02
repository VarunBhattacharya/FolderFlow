# FolderFlow: The Digital Butler 🧹

**FolderFlow** is a simple, yet powerful Python script designed to automatically organize files in a specified directory by sorting them into dedicated subfolders based on their file type (extension). Say goodbye to clutter in your Downloads or project folders!

## Features

* **Automatic Sorting:** Scans a folder and organizes files into logical categories like `Images`, `Documents`, `Videos`, etc.
* **Customizable:** Easily modify the file types dictionary to add or change categories.
* **Safe Operations:** Uses the `shutil` module for reliable file moving.

## Getting Started

### Prerequisites

You only need **Python 3.x** installed on your system. No external libraries are needed beyond Python's standard library (`os`, `shutil`).

### Installation

1.  **Clone or Download:** Get a copy of the script (`file_organizer.py`).
2.  **Define Target:** **IMPORTANT:** Open the script and change the `TARGET_DIR` variables to the absolute path of the folder you want to organize.

    ```python
    # file_organizer.py
    TARGET_DIR = "/Users/yourname/Desktop/Test_Folder_To_Organize" 
    ```

### Usage

1.  Open your terminal or command prompt.
2.  Navigate to the directory where you saved the script.
3.  Run the script:

    ```bash
    python file_organizer.py
    ```

The script will print a log of every file it moves and any folders it creates.

## Customization (File Types)

You can easily adjust the organization logic by modifying the `file_types` dictionary inside the script:

```python
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.svg'],
        'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
        # Add a new category:
        'Audio': ['.mp3', '.wav', '.flac'],
    }
