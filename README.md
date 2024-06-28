# File Organizer Script

This script helps you organize files in a specified directory into subfolders based on their file extensions. The script will move files into predefined folders like "Videos", "Audios", "Images", etc. Files with extensions not predefined will be moved to a folder specified by the user for unknown files.

## Usage

1. **Requirements**: Ensure you have Python installed on your system.

2. **Setup**: Save the script in a `.py` file.

3. **Run the Script**: Open a terminal or command prompt, navigate to the directory where your script is saved.

4. **Input the Directory**: When prompted, enter the path to the directory containing the files you want to organize.

5. **Input the Folder Name for Unknown Files**: When prompted, enter the name of the folder where files with unknown extensions should be moved.

## How it Works

1. The script first defines a dictionary `folders` where keys are folder names and values are lists of file extensions that should be moved into those folders.

2. The function `create_move(ext, file_name)` checks the extension of a file and moves it to the corresponding folder. If the extension is not found in the predefined folders, the file is moved to a folder for unknown files.

3. The script reads all files in the specified directory, checks each file's extension, and moves the file to the appropriate folder.


