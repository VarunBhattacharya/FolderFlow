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

  #TODO: Other logic to be added
  pass

#Main Method
def main():
  #Code here
  organizeFiles(TARGET_DIR)


if __name__ == "__main__":
  main()
