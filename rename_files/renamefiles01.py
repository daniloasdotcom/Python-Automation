"""Simple is better than complex. This code snippet lists all files in a specified folder and renames PDF files by
removing the first 13 characters from their names.

Explicit is better than implicit. The purpose of the code is evident: it aims to clean up PDF file names by removing
the initial characters, likely for organization or formatting reasons.

Readability counts.
The code is concise and easy to understand. Each step is clearly commented, explaining its purpose and functionality.

Now is better than never.
"""

import os

# Define the path to the folder containing the files
folder = 'C:/Users/User/Downloads/Microbiology/MicroGeneral'

# List all files in the folder
files = os.listdir(folder)

# Iterate over each file in the folder
for file in files:
    # Check if the file ends with '.pdf'
    if file.endswith('.pdf'):
        # Remove the first 13 characters from the file name
        new_name = file[13:]
        # Create the full path for the old file name
        old_path = os.path.join(folder, file)
        # Create the full path for the new file name
        new_path = os.path.join(folder, new_name)
        # Rename the file
        os.rename(old_path, new_path)
