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
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.svg'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.ppt', '.xlsx'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Scripts': ['.py', '.sh', '.js', '.html'],
    'Audio': ['.mp3', '.wav', '.flac', '.aac']
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

    print("File Organization completed.")