import os

current_directory = os.getcwd()  # Get the current working directory

# Iterate over all directories and files recursively
for root, dirs, files in os.walk(current_directory):
    for filename in files:
        file_path = os.path.join(root, filename)

        # Split the filename into words
        words = filename.split()

        # Extract the last two words
        new_filename = ' '.join(words[-2:])  # Join the last two words with a space

        # Create the new file path
        new_file_path = os.path.join(root, new_filename)

        # Rename the file
        os.rename(file_path, new_file_path)
        print(f"Renamed: {file_path} --> {new_file_path}")

input("Press Enter to exit")