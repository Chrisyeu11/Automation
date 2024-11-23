import os
import shutil
from tkinter import Tk
from tkinter.filedialog import askopenfilenames, askdirectory

def move_selected_files():
    # Initialize Tkinter and hide the root window
    Tk().withdraw()

    # Ask the user to select files to move
    print("Please select the files to move.")
    selected_files = askopenfilenames(title="Select Files to Move")
    if not selected_files:
        print("No files selected. Exiting...")
        return

    # Ask the user to select the target folder
    print("Please select the target folder.")
    target_folder = askdirectory(title="Select Target Folder")
    if not target_folder:
        print("No target folder selected. Exiting...")
        return

    # Move the selected files to the target folder
    files_moved = []
    for file in selected_files:
        file_name = os.path.basename(file)  # Extract the file name
        target_path = os.path.join(target_folder, file_name)

        # Move the file
        shutil.move(file, target_path)
        files_moved.append(file_name)

    # Provide feedback to the user
    if files_moved:
        print(f"Moved {len(files_moved)} file(s) to '{target_folder}'.")
        print("Files moved:")
        for file in files_moved:
            print(f" - {file}")
    else:
        print("No files were moved.")

# Run the function
if __name__ == "__main__":
    move_selected_files()
