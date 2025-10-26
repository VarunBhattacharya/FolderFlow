import os
import shutil
import hashlib
import threading
import sys
import time
from utils import main_heading, lined_input, error_print, lined_print, color_print, optional_input, default_directory_paths,table
from rich.console import Console

console = Console()
# Global counters
duplicates_found = 0
files_renamed = 0


def get_folder_name(file_path):
    return os.path.basename(os.path.dirname(file_path))

def file_hash(path):
    """Return SHA256 hash of a file, or None on error."""
    h = hashlib.sha256()
    try:
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                h.update(chunk)
        return h.hexdigest()
    except Exception:
        return None


def generate_new_name(dest_path):
    """Generate a unique filename if a file with the same name exists."""
    base, ext = os.path.splitext(dest_path)
    counter = 1
    new_path = f"{base}({counter}){ext}"
    while os.path.exists(new_path):
        counter += 1
        new_path = f"{base}({counter}){ext}"
    return new_path


def move_file(source, destination):
    """Move a file with duplicate detection and renaming if needed."""
    global duplicates_found, files_renamed
    if not os.path.exists(source):
        error_print(f"File not found: {source}", type="error")
        return False

    if os.path.exists(destination):
        src_hash = file_hash(source)
        dest_hash = file_hash(destination)
        if src_hash and dest_hash and src_hash == dest_hash:
            duplicates_found += 1
            error_print(f"Duplicate found, skipped: {os.path.basename(source)}", type="warning")
            return False
        else:
            new_destination = generate_new_name(destination)
            shutil.move(source, new_destination)
            files_renamed += 1
            # color_print(f"Renamed + moved {source} -> {new_destination}", color="#F9A825")
            table.add_row("Rename + Move",os.path.basename(source), get_folder_name(source), get_folder_name(destination))
            return True

    shutil.move(source, destination)
    # color_print(f"Moved {source} -> {destination}", color="#51BE9F")
    table.add_row("Move",os.path.basename(source), get_folder_name(source), get_folder_name(destination))
    return True


def categorize_file(filename, file_types):
    """Return folder name for a file based on extension."""
    _, ext = os.path.splitext(filename)
    ext = ext.lower()
    for folder, extensions in file_types.items():
        if ext in extensions:
            return folder
    return "Others"


def organize_files(directory, recursive=False):
    """Main function to organize files in a folder."""
    global duplicates_found, files_renamed
    duplicates_found = 0
    files_renamed = 0

    original_cwd = os.getcwd()
    try:
        os.chdir(directory)
    except FileNotFoundError:
        error_print(f"Directory not found: {directory}", type="error")
        return

    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.svg', '.bmp', '.tiff', '.webp', '.ico'],
        'Videos': ['.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv', '.webm'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.ppt', '.pptx', '.xls', '.xlsx', '.odt', '.rtf', '.md'],
        'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z', '.bz2', '.xz', '.iso'],
        'Scripts': ['.py', '.sh', '.js', '.html', '.css', '.ts', '.jsx', '.tsx', '.php', '.rb', '.java', '.c', '.cpp'],
        'Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a', '.wma'],
        'Fonts': ['.ttf', '.otf', '.woff', '.woff2'],
        'Executables': ['.exe', '.msi', '.bat', '.apk', '.app', '.deb', '.rpm'],
        'Spreadsheets': ['.xls', '.xlsx', '.ods', '.csv'],
        'Databases': ['.db', '.sqlite', '.sql', '.mdb', '.accdb'],
        'Code Notebooks': ['.ipynb', '.rmd'],
        '3D Models': ['.obj', '.fbx', '.stl', '.dae', '.gltf'],
        'Design Files': ['.psd', '.ai', '.xd', '.sketch', '.fig'],
        'Logs': ['.log', '.out'],
        'Configs': ['.ini', '.cfg', '.yaml', '.yml', '.toml', '.env']
    }
    category_folder_names = set(file_types.keys()) | {"Others"}

    lined_print(f"Starting organization in: {directory}", color="#F97910")

    if not recursive:
        for item in os.listdir():
            if os.path.isdir(item) or item == os.path.basename(__file__):
                continue
            dest_folder = categorize_file(item, file_types)
            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)
                lined_print(f"[CREATED] Folder: {dest_folder}", color="#8E16FF")
            move_file(os.path.join(directory, item), os.path.join(directory, dest_folder, item))
    else:
        for root, dirs, files in os.walk(directory):
            dirs[:] = [d for d in dirs if d not in category_folder_names]
            for filename in files:
                if filename == os.path.basename(__file__):
                    continue
                src_path = os.path.join(root, filename)
                dest_folder = categorize_file(filename, file_types)
                relpath = os.path.relpath(root, directory)
                if os.path.normpath(relpath).split(os.sep)[0] in category_folder_names:
                    continue
                destination_root = os.path.join(directory, dest_folder, relpath)
                if not os.path.exists(destination_root):
                    os.makedirs(destination_root)
                    lined_print(f"[CREATED] Folder: {destination_root}", color="#8E16FF")
                move_file(src_path, os.path.join(destination_root, filename))

    lined_print("File organization completed.", color="green", line_style="=*=")
    color_print(f"Duplicates found: {duplicates_found}", color="#FF6F61")
    color_print(f"Files renamed: {files_renamed}", color="#FF6F61")

    try:
        os.chdir(original_cwd)
    except Exception:
        pass

confirmation_input = None
def get_input():
    global confirmation_input
    confirmation_input = input("Confirm (y/yes)")

def main():
    global confirmation_input
    main_heading("FOLDER FLOW", "FolderFlow: Auto-Sort Files by Type, Instantly!")

    #default folder location or manual input
    desktop_location, downloads_location = default_directory_paths()
    target_dir = optional_input("Choose an option or put your own directory path",["Downlaods","Desktop"],"Downloads","Target Directory")
    if(target_dir.lower() == "downloads" or target_dir == "1"):
        target_dir = downloads_location
    elif(target_dir.lower()=="desktop" or target_dir == "2"):
        target_dir = desktop_location
    lined_print(f"Target Directory>>> {target_dir}")
    error_print("The Process is IRREVERSIBLE please confirm with (y/yes), ABORTING in 10 sec...",type="warning")
    

    input_thread = threading.Thread(target = get_input )
    input_thread.daemon = True
    input_thread.start()
    input_thread.join(timeout=10)
    
    if(confirmation_input and confirmation_input.strip().lower() in ['y','yes']):
        # print("User types: org begins ", confirmation_input)
        lined_print("Organization Confirmed!")
        organize_files(target_dir, recursive=False)
    else:
        print()
        error_print("You didn't confirmed! Program Quit", type="error")
    console.print(table)



if __name__ == "__main__":
    main()
