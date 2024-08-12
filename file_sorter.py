import os
import shutil


path=input("Enter directory path: ")
path+='/'
file_names = os.listdir(path)

# Define the folder names and their corresponding file extensions
folder_details = {
    'pdf files': ['.pdf'],
    'images': ['.png', '.jpg', '.jpeg'],
    'documents': ['.docx', '.xlsx', '.pptx'],
    'excel files': ['.xlsx'],
    'videos': ['.mp4', '.avi', '.mov', '.mkv'],
    'audio files': ['.mp3', '.wav'],
    'compressed files': ['.zip', '.rar'],
    'others': ['.txt', '.exe', '.dll', '.dll', '.msi', '.pdb', '.dll', '.ico']  # Add more file extensions as needed
}

# Check which types of files exist and create corresponding folders if needed
existing_folders = set()

for file in file_names:
    for folder_name, extensions in folder_details.items():
        if any(file.endswith(ext) for ext in extensions):
            existing_folders.add(folder_name)

# Create folders only if they are in the existing_folders set
for folder_name in existing_folders:
    folder_path = os.path.join(path, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Move files to the corresponding folders
for file in file_names:
    for folder_name, extensions in folder_details.items():
        if any(file.endswith(ext) for ext in extensions):
            src = os.path.join(path, file)
            dest = os.path.join(path, folder_name, file)
            if not os.path.exists(dest):
                shutil.move(src, dest)

print("Files sorted successfully!")
