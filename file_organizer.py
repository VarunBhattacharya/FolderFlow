import os
import shutil
from utils import main_heading, lined_input, error_print, lined_print, color_print

#Main heading
main_heading("FOLDER FLOW", "FolderFlow: Auto-Sort Files by Type, Instantly!")

from utils import main_heading, lined_input, error_print, lined_print, color_print

#Main heading
main_heading("FOLDER FLOW", "FolderFlow: Auto-Sort Files by Type, Instantly!")


TARGET_DIR = lined_input("Enter folder path to organize")
TARGET_DIR = lined_input("Enter folder path to organize")

def moveFile(source,destination):
  #move a file from its source path to a destination path
  try:
      if not os.path.exists(source):
          error_print(f"File not found at {source}", type="error")
          error_print(f"File not found at {source}", type="error")
          return False
      if os.path.exists(destination):
          error_print(f"File already exists at {destination}, skipping.", type="warning")
          error_print(f"File already exists at {destination}, skipping.", type="warning")
          return False
      shutil.move(source, destination)
      color_print(f"move {source} -> {destination}",color="cyan",color="cyan")
      return True
  except (shutil.Error, OSError) as e:
      error_print(f"Error moving {source} to {destination}: {e}", type="error")
      error_print(f"Error moving {source} to {destination}: {e}", type="error")
      return False
  
def organizeFiles(directory, recursive=False):
  #changes the current working directory to the target directory
  original_cwd = os.getcwd()
  try:
    os.chdir(directory)
  except FileNotFoundError:
    error_print(f"Directory not found at {directory}", type="error")
    return
  try:
    lined_print(f"Starting organization in: {directory}", color="#F97910")

    # Added file types dictionary which will be parsed later on as part of issue-2
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

    # Build set of category folder names to help skip during recursion
    category_folder_names = set(file_types.keys()) | {"Others"}

    def categorize_extension(filename):
      _, extension = os.path.splitext(filename)
      extension = extension.lower()
      destFolder = "Others"
      for folder, extensions in file_types.items():
        if extension in extensions:
          destFolder = folder
          break
      return destFolder

    if not recursive:
      for item in os.listdir():
        if os.path.isdir(item):
          continue
        if item == os.path.basename(__file__):
          continue
        destFolder = categorize_extension(item)
        if not os.path.exists(destFolder):
          os.makedirs(destFolder)
          lined_print(f"[CREATED] Folder: {destFolder}", color="#8E16FF")
        srcpath = os.path.join(directory, item)
        despath = os.path.join(directory, destFolder, item)
        moveFile(srcpath, despath)
    else:
      # Recursive mode: walk all files and maintain relative structure
      for root, dirs, files in os.walk(directory):
        # Avoid descending into any category folder anywhere in tree
        dirs[:] = [d for d in dirs if d not in category_folder_names]

        for filename in files:
          if filename == os.path.basename(__file__):
            continue
          srcpath = os.path.join(root, filename)
          destFolder = categorize_extension(filename)
          relpath = os.path.relpath(root, directory)

          top_level_dirname = os.path.normpath(relpath).split(os.sep)[0] if relpath not in (".", "") else ""
          if top_level_dirname in category_folder_names:
            continue

          destination_root = os.path.join(directory, destFolder, relpath)
          if not os.path.exists(destination_root):
            os.makedirs(destination_root)
            lined_print(f"[CREATED] Folder: {destination_root}", color="#8E16FF")

          despath = os.path.join(destination_root, filename)
          if os.path.exists(despath):
            lined_print(f"[SKIPPED] {filename} already exists in {destination_root}", color="#40A7FB")
            continue
          moveFile(srcpath, despath)

      lined_print("File organization completed.", color="green", line_style="=*=")
  finally:
    # restore original working directory to avoid side effects
    try:
      os.chdir(original_cwd)
    except Exception:
      pass


#Main Method
def main():
  target = input("Enter folder path to organize: ")
  organizeFiles(target, recursive=False)


if __name__ == "__main__":
  main()
