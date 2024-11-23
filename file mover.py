import os
import shutil
from tkinter import Tk
from tkinter.filedialog import askdirectory

def move_files_by_name():
    # Initialize Tkinter and hide the root window
    Tk().withdraw()

    # Ask the user to select the source folder
    print("Please select the source folder.")
    source_folder = askdirectory(title="Select Source Folder")
    if not source_folder:
        print("No source folder selected. Exiting...")
        return

    # Ask the user to select the target folder
    print("Please select the target folder.")
    target_folder = askdirectory(title="Select Target Folder")
    if not target_folder:
        print("No target folder selected. Exiting...")
        return

    # Get the specific name to match files
    file_name = input("Enter the specific name (or keyword) of the files to move: ").strip()

    # Iterate through files in the source folder
    files_moved = []
    for file in os.listdir(source_folder):
        if file_name in file:  # Check if the specific name is part of the file name
            source_path = os.path.join(source_folder, file)
            target_path = os.path.join(target_folder, file)

            # Move the file
            shutil.move(source_path, target_path)
            files_moved.append(file)

    # Provide feedback to the user
    if files_moved:
        print(f"Moved {len(files_moved)} file(s) containing '{file_name}' to '{target_folder}'.")
        print("Files moved:")
        for file in files_moved:
            print(f" - {file}")
    else:
        print(f"No files containing '{file_name}' were found in '{source_folder}'.")

# Run the function
if __name__ == "__main__":
    move_files_by_name()
