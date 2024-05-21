"""
This script edits a base Word file to update the week number mentioned inside it.
The base Word file (Week21_2024.docx) is located at a specified path. The script
searches for a specific text ("Semana letiva número 21") inside the Word file
and replaces it with the current week number.

The edit_word_file function takes the file path and the week number as input, opens
the Word file using the Document class from the docx module, searches for the specific
text, replaces it with the current week number, and saves the changes back to the file.

The main function is responsible for creating new files for each week from Week22_2024
to Week23_2024 based on the base Word file. For each new file created, it also calls
the edit_word_file function to update the week number inside the file.

Python modules used:
- os: Provides functions for interacting with the operating system.
- docx: Provides classes for working with Word documents.
- shutil: Provides high-level file operations.

The script follows Python best practices for readability and maintainability.

Now is better than never.
"""
import os
from docx import Document
import shutil


def edit_word_file(file_path, week_number):
    try:
        doc = Document(file_path)
        for paragraph in doc.paragraphs:
            if "Semana letiva número 21" in paragraph.text:
                paragraph.text = paragraph.text.replace("Semana letiva número 21",
                                                        f"Semana letiva número {week_number}")
        doc.save(file_path)
        print(f"File {file_path} edited successfully!")
    except Exception as e:
        print(f"Error editing file {file_path}: {e}")


def main():
    base_file = "C:/path/Week21_2024.docx"  # Insert the path of your base Word file here
    base_dest_path = "C:/path/destination"  # Insert the directory path where the new files will be saved here

    # Checking if the base file exists
    if not os.path.isfile(base_file):
        print("The base file was not found.")
        return

    # Creating files Week22_2024 through Week23_2024 based on Week21_2024 file and editing the internal content
    for week_number in range(22, 24):
        new_file_name = f"Week{week_number}_2024.docx"
        new_file_path = os.path.join(base_dest_path, new_file_name)
        shutil.copyfile(base_file, new_file_path)
        edit_word_file(new_file_path, week_number)
        print(f"File {new_file_name} created and edited successfully!")


if __name__ == "__main__":
    main()
