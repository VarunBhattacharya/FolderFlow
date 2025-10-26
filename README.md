#  FolderFlow 

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Hacktoberfest](https://img.shields.io/badge/Hacktoberfest-2025-orange.svg)](https://hacktoberfest.com/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTORS.md)

> **Your Digital Butler for Instant File Organization** 
>
> Stop wasting time sorting files manually. FolderFlow automatically organizes your cluttered folders with beautiful CLI feedback and smart duplicate detection!

---

##  What Problem Does It Solve?

Ever downloaded hundreds of files and ended up with a chaotic Downloads folder? Tired of manually sorting vacation photos, work documents, and random PDFs? **FolderFlow solves this!**

### Real-World Use Cases

*  **Messy Downloads Folder**: Organize 1000+ mixed files in seconds
*  **Student Projects**: Sort code files, documents, and resources automatically
*  **Photo Management**: Separate images, videos, and raw files instantly
*  **Work Files**: Keep documents, spreadsheets, and presentations organized
*  **Desktop Cleanup**: Transform desktop chaos into organized bliss
*  **Archive Management**: Organize old backup folders with recursive mode

---

##  Features

### Core Functionality

*  **Beautiful Rich CLI** - Color-coded output with tables and progress indicators
*  **Smart Categorization** - 16 file type categories (Images, Videos, Documents, etc.)
*  **Duplicate Detection** - SHA256 hash-based duplicate identification
*  **Automatic Renaming** - Renames files intelligently to avoid conflicts (file.txt  file(1).txt)
*  **Recursive Mode** - Organize entire directory trees, not just top-level files
*  **Quick Presets** - One-click organization for Desktop/Downloads folders
*  **Safety First** - 10-second confirmation timeout prevents accidental organization
*  **Summary Reports** - Detailed table showing all file movements
*  **Customizable** - Easily add new file type categories

### Supported File Types

| Category | Extensions |
|----------|-----------|
|  Images | `.jpg`, `.jpeg`, `.png`, `.gif`, `.svg`, `.bmp`, `.tiff`, `.webp`, `.ico` |
|  Videos | `.mp4`, `.mov`, `.avi`, `.mkv`, `.flv`, `.wmv`, `.webm` |
|  Documents | `.pdf`, `.doc`, `.docx`, `.txt`, `.ppt`, `.pptx`, `.odt`, `.rtf`, `.md` |
|  Archives | `.zip`, `.rar`, `.tar`, `.gz`, `.7z`, `.bz2`, `.xz`, `.iso` |
|  Scripts | `.py`, `.sh`, `.js`, `.html`, `.css`, `.ts`, `.jsx`, `.tsx`, `.php`, `.rb`, `.java`, `.c`, `.cpp` |
|  Audio | `.mp3`, `.wav`, `.flac`, `.aac`, `.ogg`, `.m4a`, `.wma` |
|  Fonts | `.ttf`, `.otf`, `.woff`, `.woff2` |
|  Executables | `.exe`, `.msi`, `.bat`, `.apk`, `.app`, `.deb`, `.rpm` |
|  Spreadsheets | `.xls`, `.xlsx`, `.ods`, `.csv` |
|  Databases | `.db`, `.sqlite`, `.sql`, `.mdb`, `.accdb` |
|  Notebooks | `.ipynb`, `.rmd` |
|  Design Files | `.psd`, `.ai`, `.xd`, `.sketch`, `.fig` |
|  Logs | `.log`, `.out` |
|  Configs | `.ini`, `.cfg`, `.yaml`, `.yml`, `.toml`, `.env` |

---

##  Quick Start

Get organized in 30 seconds!

```bash
# 1. Clone the repository
git clone https://github.com/VarunBhattacharya/FolderFlow.git
cd FolderFlow

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run FolderFlow
python file_organizer.py

# 4. Choose Downloads or Desktop (or enter custom path)
# 5. Confirm with 'y' within 10 seconds
# 6. Watch the magic happen! 
```

---

##  Installation

### Prerequisites

* **Python 3.8+** (tested on 3.8, 3.9, 3.10, 3.11, 3.12, 3.13)
* **pip** (Python package manager)
* **Required Libraries**:
  * `rich` - For beautiful terminal output with colors, tables, and panels

> **Note:** This project requires the `rich` library and is **not** limited to Python's standard library.

### Step-by-Step Installation

**Option 1: Standard Installation**

```bash
git clone https://github.com/VarunBhattacharya/FolderFlow.git
cd FolderFlow
pip install -r requirements.txt
```

**Option 2: Direct Download**

1. Download the [latest release](https://github.com/VarunBhattacharya/FolderFlow/releases)
2. Extract the ZIP file
3. Open terminal in the extracted folder
4. Run: `pip install -r requirements.txt`

---

##  Usage


```bash
python file_organizer.py
```

Follow the beautiful CLI prompts:

1. **Choose preset** (Downloads/Desktop) or enter custom path
2. **Review target directory**
3. **Confirm organization** (type `y` or `yes` within 10 seconds)
4. **View results** in the summary table

### Screenshots


> <img width="828" height="1018" alt="image" src="https://github.com/user-attachments/assets/039a9b84-0db3-473e-98e5-00ff1d4595dd" />

---

##  Customization

### Adding New File Categories

Open `file_organizer.py` and modify the `file_types` dictionary:

```python
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.svg', '.bmp', '.tiff', '.webp', '.ico'],
    # Add your custom category:
    'Ebooks': ['.epub', '.mobi', '.azw3'],
    'Virtual Machines': ['.ova', '.vmdk', '.vdi'],
}
```

### Customizing Presets

Edit the `default_directory_paths()` function in `utils.py` to add your favorite folders:

```python
def default_directory_paths():
    home_dir = expanduser("~")
    desktop_path = home_dir + "\\Desktop"
    downloads_path = home_dir + "\\Downloads"
    return desktop_path, downloads_path
```

---

##  Testing

FolderFlow includes comprehensive unit tests to ensure reliability.

### Run Tests

```bash
python -m unittest test.py
```

### Test Coverage

*  File movement validation
*  Folder creation verification
*  Duplicate detection
*  Error handling for missing files
*  Temporary directory cleanup

---

##  Contributing

We  contributions! FolderFlow is part of **Hacktoberfest 2025** and welcomes developers of all skill levels.

### How to Contribute

1. **Fork the repository**
2. **Create a feature branch**

   ```bash
   git checkout -b feature/amazing-feature
   ```

3. **Make your changes**
4. **Run tests** to ensure nothing breaks

   ```bash
   python -m unittest test.py
   ```

5. **Commit with clear messages**

   ```bash
   git commit -m "Add: Feature description"
   ```

6. **Push to your fork**

   ```bash
   git push origin feature/amazing-feature
   ```

7. **Open a Pull Request**

### Contribution Ideas

####  Beginner-Friendly

* Add more file type categories
* Fix typos or improve documentation
* Add docstrings to functions
* Create example screenshots

####  Intermediate

* Add configuration file support (JSON/YAML)
* Implement `--dry-run` mode
* Add file size filtering options
* Create a progress bar for large folders
* Add colorblind-friendly themes

####  Advanced

* Build a GUI version (tkinter/PyQt)
* Implement watch mode (auto-organize on file creation)
* Add undo/rollback functionality
* Organize by date (Year/Month folders)
* Multi-language support
* Create installer/package for Windows/Mac/Linux

Check out our [Contributors Guide](CONTRIBUTORS.md) for more details!

---

##  Project Stats

```text
 file_organizer.py    # Main organization logic (187 lines)
 utils.py             # CLI utilities & styling (106 lines)
 test.py              # Unit tests
 requirements.txt     # Dependencies (rich library)
 CONTRIBUTORS.md      # Hall of fame
 README.md            # You are here!
```

**Total Lines of Code:** ~300+

**Dependencies:** 1 (`rich` for beautiful CLI)

**Test Coverage:** Core functionality covered

---

##  License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

**TL;DR:** You can use, modify, and distribute this project freely! 

---

##  Contributors

Thanks to all the amazing people who have contributed to FolderFlow! 

See the full list in [CONTRIBUTORS.md](CONTRIBUTORS.md)

---

##  Acknowledgments

* Built with  using [Rich](https://github.com/Textualize/rich) for beautiful terminal output
* Inspired by the chaos of Downloads folders everywhere
* Created for **Hacktoberfest 2025**

---

##  Support & Contact

*  **Found a bug?** [Open an issue](https://github.com/VarunBhattacharya/FolderFlow/issues)
*  **Have a suggestion?** [Start a discussion](https://github.com/VarunBhattacharya/FolderFlow/discussions)
*  **Like the project?** Star it on GitHub!

---

<div align="center">

**Made with  and  by the FolderFlow Community**

 **Star this repo if FolderFlow helped organize your digital life!** 

</div>

---

##  FAQ

**Q: Will FolderFlow delete my files?**

A: No! FolderFlow only **moves** files, never deletes them. All files remain safe.

**Q: What happens if two files have the same name?**

A: FolderFlow checks if they're duplicates using SHA256 hash. Duplicates are skipped; different files are renamed (e.g., `file(1).txt`).

**Q: Can I undo organization?**

A: Currently, no automatic undo. We recommend testing on a backup folder first. Undo feature is planned for future releases!

**Q: Does it work on Windows/Mac/Linux?**

A: Yes! FolderFlow is cross-platform (though default presets are Windows-optimized).

**Q: Is my data safe?**

A: FolderFlow operates locally on your machine. No data is sent anywhere. It's open source—review the code yourself!
