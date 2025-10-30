import unittest
import os
import shutil
import tempfile
from file_organizer import organizeFiles

class TestFileOrganizer(unittest.TestCase):
    
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

        self.test_files= {
            "script.py": "Scripts",
            "document.txt": "Documents",
            "image.jpg": "Images",
            "archive.zip": "Archives",
            "video.mp4": "Videos",
            "other.log": "Others"
        }

        self.initial_paths = []
        self.expected_paths = {}
        
        for filename, folder_name in self.test_files.items():
            initial_path = os.path.join(self.test_dir,filename)

            with open(initial_path,"w") as f:
                f.write("test content")

            self.initial_paths.append(initial_path)

            expected_folder = os.path.join(self.test_dir, folder_name)
            expected_final_path = os.path.join(expected_folder, filename)
            
            self.expected_paths[filename] = expected_final_path

    def tearDown(self):
        try:
            shutil.rmtree(self.test_dir)
        except OSError as e:
            print(f"Error during cleanup of temporary directory {self.test_dir}: {e}")

    def test_file_move(self):
        
        organizeFiles(self.test_dir)

        for filename,expected_path in self.expected_paths.items():
            self.assertTrue(
                os.path.exists(expected_path),
                f"Assertion failed: File '{filename}' was NOT found at its expected location: {expected_path}"
            )

        for initial_path in self.initial_paths:
                            self.assertFalse(
                os.path.exists(initial_path), 
                f"Assertion failed: File was found at its OLD location: {initial_path}. It should have been moved."
            )
        
        for folder_name in set(self.test_files.values()):
            folder_path = os.path.join(self.test_dir, folder_name)
            self.assertTrue(
                os.path.isdir(folder_path), 
                f"Assertion failed: Folder '{folder_name}' was not created or is not a directory."
            )

if __name__=="__main__":
     unittest.main()