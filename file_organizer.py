#Imports
import os
import shutil

TARGET_DIR = "/folder-to-organize"  # need to change from user to user

def organizeFiles(directory):
    # changes the current working directory to the target directory
    try:
        os.chdir(directory)
    except FileNotFoundError:
        print(f"Error: Directory not found at {directory}")
        return
    except PermissionError:
        print(f"Error: Permission denied to access {directory}")
        return
    except Exception as e:
        print(f"Unexpected error while changing directory: {e}")
        return

    print(f"Starting organization in: {directory}")

    # Added file types dictionary
    fileTypes = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.svg'],
        'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.ppt', '.xlsx'],
        'Archives': ['.zip', '.rar', '.tar', '.gz'],
        'Scripts': ['.py', '.sh', '.js', '.html'],
        'Audio': ['.mp3', '.wav', '.flac', '.aac']
    }

    try:
        items = os.listdir()
    except Exception as e:
        print(f"Error listing items in directory: {e}")
        return

    for item in items:
        if os.path.isdir(item):
            continue

        # skip the script itself
        if item == os.path.basename(__file__):
            continue

        _, extension = os.path.splitext(item)
        extension = extension.lower()

        # default folder
        destFolder = "Others"
        for folder, extensions in fileTypes.items():
            if extension in extensions:
                destFolder = folder
                break

        # create folder if not exists
        if not os.path.exists(destFolder):
            try:
                os.makedirs(destFolder)
                print(f"[CREATED] Folder: {destFolder}")
            except Exception as e:
                print(f"Error creating folder '{destFolder}': {e}")
                continue

        destPath = os.path.join(destFolder, item)

        # ✅ Move file with error handling
        try:
            shutil.move(item, destPath)
            print(f"Moved: {item} → {destFolder}")
        except shutil.Error as e:
            print(f"Shutil error while moving '{item}': {e}")
        except Exception as e:
            print(f"Unexpected error moving '{item}': {e}")

    print("File Organization completed.")

# Main Method
def main():
    organizeFiles(TARGET_DIR)

if __name__ == "__main__":
    main()
