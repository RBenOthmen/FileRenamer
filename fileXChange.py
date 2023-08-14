import os
import tkinter as tk
from tkinter import filedialog

def change_extension(directory, new_extension):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if '.' in filename:  # Ensure the file has an extension
                name, _ = os.path.splitext(filename)
                new_filename = f"{name}.{new_extension}"
                file_path = os.path.join(root, filename)
                new_file_path = os.path.join(root, new_filename)
                os.rename(file_path, new_file_path)
                print(f"Renamed: {file_path} --> {new_file_path}")

def on_entry_click(event):
    if extension_entry.get() == "e.g. pdf":
        extension_entry.delete(0, "end")
        extension_entry.config(fg="black")  # Change text color

def on_focus_out(event):
    if not extension_var.get():
        extension_entry.insert(0, "e.g. pdf")
        extension_entry.config(fg="gray")  # Change text color

def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        new_extension = extension_var.get()
        change_extension(folder_selected, new_extension)
        status_label.config(text="Extensions changed successfully!")

# Create the main window
root = tk.Tk()
root.title("Extension Changer")
root.geometry("400x200")  # Set the window size
root.configure(bg="#333333")  # Set the background color

# Center the window on the screen
window_width = root.winfo_reqwidth()
window_height = root.winfo_reqheight()
position_right = int(root.winfo_screenwidth() / 2 - window_width / 2)
position_down = int(root.winfo_screenheight() / 2 - window_height / 2)
root.geometry(f"+{position_right}+{position_down}")

# Create a label
label = tk.Label(root, text="Select a folder to change file extensions:", fg="white", bg="#333333")
label.pack(pady=10)

# Create an entry field for the new extension with a placeholder
extension_var = tk.StringVar()
extension_entry = tk.Entry(root, textvariable=extension_var, fg="gray")
extension_entry.insert(0, "e.g. pdf")  # Placeholder text
extension_entry.bind("<FocusIn>", on_entry_click)  # Bind click event
extension_entry.bind("<FocusOut>", on_focus_out)  # Bind focus out event
extension_entry.pack()

# Create a button to browse for a folder
browse_button = tk.Button(root, text="Browse", command=browse_folder, bg="darkgray", fg="white")
browse_button.pack(pady=15)  # Increased padding
browse_button.config(width=20)  # Increased button width

# Create a label to display status
status_label = tk.Label(root, text="", fg="green", bg="#333333")
status_label.pack()

# Start the GUI event loop
root.mainloop()
