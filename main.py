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
        status_label.config(text="Files renamed successfully!", fg="green")

# Create the main window
root = tk.Tk()
root.title("File Renamer")

# Set a dark theme color scheme
root.configure(bg="#333333")
root.option_add("*TButton*Background", "#444444")
root.option_add("*TButton*Foreground", "white")
root.option_add("*Label*Background", "#333333")
root.option_add("*Label*Foreground", "white")
root.option_add("*TLabel*Background", "#333333")
root.option_add("*TLabel*Foreground", "white")

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the x and y coordinates to center the window
x = (screen_width - 400) // 2  # Adjusted window width
y = (screen_height - 250) // 2  # Adjusted window height

root.geometry(f"400x250+{x}+{y}")  # Set window size and position

# Create a label
label = tk.Label(root, text="Select a folder to rename files:")
label.pack(pady=20)

# Create a button to browse for a folder
browse_button = tk.Button(root, text="Browse", command=browse_folder, padx=20, pady=10)
browse_button.pack()

# Create a label to display status
status_label = tk.Label(root, text="", fg="green")
status_label.pack(pady=20)

# Start the GUI event loop
root.mainloop()
