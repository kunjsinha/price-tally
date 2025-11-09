import shutil
import os
import platform

def download_file(file_name):
    system = platform.system()
    if system == "Android":
        downloads_folder = "/storage/emulated/0/Download"
    else:
        downloads_folder = os.path.expanduser("~/Downloads")

    # Ensure the Downloads folder exists
    if not os.path.exists(downloads_folder):
        os.makedirs(downloads_folder)

    # Full destination path
    destination = os.path.join(downloads_folder, os.path.basename(file_name))

    # Check if source file exists first
    if os.path.exists(file_name):
        shutil.copy(file_name, destination)
        # print(f"Copied {file_name} to {destination}")
    else:
        pass
        # print(f"File {file_name} not found in current directory")
