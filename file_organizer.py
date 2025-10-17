import os
import shutil

def moveFile(source,destination):
  #move a file from its source path to a destination path
  try:
      if not os.path.exists(source):
          print(f"Error: File not found at {source}")
          return False
      if os.path.exists(destination):
          print(f"Warning: File already exists at {destination}, skipping.")
          return False
      shutil.move(source, destination)
      print(f"move {source} -> {destination}")
      return True
  except (shutil.Error, OSError) as e:
      print(f"Error moving {source} to {destination}: {e}")
      return False
  
def organizeFiles(directory, recursive=False):
  #changes the current working directory to the target directory
  original_cwd = os.getcwd()
  try:
    os.chdir(directory)
  except FileNotFoundError:
    print(f"Error: Directory not found at {directory}")
    return
  try:
    print(f"Starting organization in: {directory}")

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
          print(f"[CREATED] Folder: {destFolder}")
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
            print(f"[CREATED] Folder: {destination_root}")

          despath = os.path.join(destination_root, filename)
          if os.path.exists(despath):
            print(f"[SKIPPED] {filename} already exists in {destination_root}")
            continue
          moveFile(srcpath, despath)

      print("File organization completed.")
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
