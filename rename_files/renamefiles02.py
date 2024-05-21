"""Beautiful is better than ugly. This code snippet iterates through files in a directory, specifically targeting PDF
files with names starting with 'nexojornal.com.br-'. If a file meets these criteria, it removes the prefix
'nexojornal.com.br-' from its name and renames it.

Explicit is better than implicit. The intent of the code is clear: it aims to clean up the filenames of PDF files
from a specific source, making them more concise and readable.

Simple is better than complex. The process is straightforward: it checks each file, performs a simple string
manipulation to remove the prefix, and then renames the file.

Complex is better than complicated. While the task might seem complex due to the manipulation of file names,
the code itself remains simple and easy to understand.

Readability counts. The code uses descriptive variable names and comments to enhance readability, ensuring that its
purpose is clear to anyone reviewing it.

Now is better than never.
"""

import os  # Import the os module for interacting with the operating system

# Define the path to the directory containing the files
path = 'C:/path'

# List all files in the specified directory
files = os.listdir(path)

# Iterate through each file in the directory
for file in files:
    # Check if the file ends with '.pdf' and starts with 'nexojornal.com.br-'
    if file.endswith('.pdf') and file.startswith('nexojornal.com.br-'):
        # Remove the 'nexojornal.com.br-' prefix from the file name
        new_name = file.replace('nexojornal.com.br-', '')
        # Create the full old file path by joining the directory path and the original file name
        old_path = os.path.join(path, file)
        # Create the full new file path by joining the directory path and the new file name
        new_path = os.path.join(path, new_name)
        # Rename the file from old_path to new_path
        os.rename(old_path, new_path)

