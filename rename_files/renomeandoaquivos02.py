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

