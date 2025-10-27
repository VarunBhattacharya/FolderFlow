import os
from rich.table import Table
from rich import box
from rich.console import Console
from rich.align import Align

console = Console()


def categorize_file(filename, file_types):
    """Return folder name for a file based on extension."""
    _, ext = os.path.splitext(filename)
    ext = ext.lower()
    for folder, extensions in file_types.items():
        if ext in extensions:
            return folder
    return "Others"


table = Table(
    title="Operation Preview",
    box=box.SQUARE,
    show_header=True,
    header_style="bold #FEAB06",
    border_style="bright_green",
)
table.add_column("File Name")
table.add_column("Destination")


def dry_run_test(target, file_types):
    for item in os.listdir(target):
        # print(f"current file: {item}", end=" | ")
        # print(categorize_file(item, file_types))
        destination = categorize_file(item, file_types)
        table.add_row(item,destination)
    console.print(Align.center(table))


if __name__ == "__main__":
    file_types = {
        "Images": [
            ".jpg",
            ".jpeg",
            ".png",
            ".gif",
            ".svg",
            ".bmp",
            ".tiff",
            ".webp",
            ".ico",
        ],
        "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv", ".webm"],
        "Documents": [
            ".pdf",
            ".doc",
            ".docx",
            ".txt",
            ".ppt",
            ".pptx",
            ".xls",
            ".xlsx",
            ".odt",
            ".rtf",
            ".md",
        ],
        "Archives": [".zip", ".rar", ".tar", ".gz", ".7z", ".bz2", ".xz", ".iso"],
        "Scripts": [
            ".py",
            ".sh",
            ".js",
            ".html",
            ".css",
            ".ts",
            ".jsx",
            ".tsx",
            ".php",
            ".rb",
            ".java",
            ".c",
            ".cpp",
        ],
        "Audio": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a", ".wma"],
        "Fonts": [".ttf", ".otf", ".woff", ".woff2"],
        "Executables": [".exe", ".msi", ".bat", ".apk", ".app", ".deb", ".rpm"],
        "Spreadsheets": [".xls", ".xlsx", ".ods", ".csv"],
        "Databases": [".db", ".sqlite", ".sql", ".mdb", ".accdb"],
        "Code Notebooks": [".ipynb", ".rmd"],
        "3D Models": [".obj", ".fbx", ".stl", ".dae", ".gltf"],
        "Design Files": [".psd", ".ai", ".xd", ".sketch", ".fig"],
        "Logs": [".log", ".out"],
        "Configs": [".ini", ".cfg", ".yaml", ".yml", ".toml", ".env"],
    }
    dry_run_test(file_types)
