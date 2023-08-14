import os
import tkinter as tk
from tkinter import filedialog

def rename_files(directory):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            words = filename.split()
            new_filename = ' '.join(words[-2:])
            new_file_path = os.path.join(root, new_filename)
            os.rename(file_path, new_file_path)
            print(f"Renamed: {file_path} --> {new_file_path}")

def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        rename_files(folder_selected)
        status_label.config(text="Files renamed successfully!")

# Create the main window
root = tk.Tk()
root.title("File Renamer")

# Create a label
label = tk.Label(root, text="Select a folder to rename files:")
label.pack(pady=10)

# Create a button to browse for a folder
browse_button = tk.Button(root, text="Browse", command=browse_folder)
browse_button.pack()

# Create a label to display status
status_label = tk.Label(root, text="", fg="green")
status_label.pack(pady=10)

# Start the GUI event loop
root.mainloop()