import os
import shutil

TARGET_DIR = "/folder-to-organize" #need to change from user to user

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
  
def organizeFiles(directory):
  #changes the current working directory to the target directory
  try:
    os.chdir(directory)
  except FileNotFoundError:
    print(f"Error: Directory not found at {directory}")
    return

  print(f"Starting organization in: {directory}")
  
  #Added file types dictionary which will be parsed later on as part of issue-2
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

  for item in os.listdir():
    if os.path.isdir(item):
        continue 
    
    #case: if the item is the main script itself
    if item == os.path.basename(__file__):
        continue
    
    _, extension = os.path.splitext(item) 
    extension = extension.lower() #normalizing the extension to smaller case if any

    #check for finding the extension if available in fileTypes dictionary
    destFolder = "Others"
    for folder, extensions in file_types.items():
      if extension in extensions:
          destFolder = folder
          break
    
    #if destination folder doesn't exist then below part will create it.
    if not os.path.exists(destFolder):
        os.makedirs(destFolder)
        print(f"[CREATED] Folder: {destFolder}")
    
    srcpath=os.path.join(directory,item)
    despath=os.path.join(directory,destFolder,item)
    moveFile(srcpath,despath)

    #TODO: Add logic for moving the code to destination path and throw error correspondingly.

    print("File Organization completed.")


#Main Method
def main():
  #Code here
  organizeFiles(TARGET_DIR)


if __name__ == "__main__":
  main()
