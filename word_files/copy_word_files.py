"""
Simple is better than complex.
This script creates copies of a base Word file for each week from Week22_2024 to Week30_2024.
The base Word file (Week21_2024.docx) is located at a specified path. The copies are created
in a designated directory.

Readability counts.
The shutil module is used for file operations, and the os module
is used for interacting with the operating system. The script checks if the base file exists
before proceeding with file copying. Each new file is named according to the week number
and the year (2024) and is created by copying the content of the base file using shutil.copyfile().
A success message is printed for each new file created.

There should be one-- and preferably only one --obvious way to do it.
This script follows Python best practices for readability and maintainability.

Now is better than never.
"""

import shutil  # Import shutil module for file operations
import os  # Import os module for interacting with the operating system

def main():
    base_file = "C:/path/Week21_2024.docx"  # Path to the base Word file
    base_dest_path = "C:/path/destination"  # Directory path where new files will be saved

    # Check if the base file exists
    if not os.path.isfile(base_file):
        print("The base file was not found.")
        return

    # Create files Week22_2024 through Week30_2024 based on Week21_2024 file
    for week_number in range(22, 31):
        new_file_name = f"Week{week_number}_2024.docx"
        new_file_path = os.path.join(base_dest_path, new_file_name)
        shutil.copyfile(base_file, new_file_path)
        print(f"File {new_file_name} created successfully!")

if __name__ == "__main__":
    main()

