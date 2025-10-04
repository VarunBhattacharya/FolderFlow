#Imports
import os
import shutil

TARGET_DIR = "/folder-to-organize" #need to change from user to user

def organizeFiles(directory):
  #changes the current working directory to the target directory
  try:
    os.chdir(directory)
  except FileNotFoundError:
    print(f"Error: Directory not found at {directory}")
    return

  print(f"Starting organization in: {directory}")
  
  #Added file types dictionary which will be parsed later on as part of issue-2
  fileTypes = {
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
    
    destPath = os.path.join(destFolder, item)

    #TODO: Add logic for moving the code to destination path and throw error correspondingly.

    print("File Organization completed.")


#Main Method
def main():
  #Code here
  organizeFiles(TARGET_DIR)


if __name__ == "__main__":
  main()
