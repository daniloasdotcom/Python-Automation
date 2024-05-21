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
