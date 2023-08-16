from pytube import YouTube
import tkinter as tk
from tkinter import messagebox

def on_entry_click(event):
    if url_entry.get() == placeholder_text:
        url_entry.delete(0, "end")
        url_entry.config(fg="white")

def on_focus_out(event):
    if url_entry.get() == "":
        url_entry.insert(0, placeholder_text)
        url_entry.config(fg="gray")

def download_video():
    url = url_entry.get()
    try:
        yt = YouTube(url)
        video_stream = yt.streams.get_highest_resolution()
        video_stream.download(output_path="./")
        messagebox.showinfo("Download Successful", "Video downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def download_audio():
    url = url_entry.get()
    try:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_stream.download(output_path="./")
        messagebox.showinfo("Download Successful", "Audio downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create GUI
root = tk.Tk()
root.title("YouTube Downloader")
root.configure(bg="#333333")  # Set background color

# Center the window
window_width = 400
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width - window_width) // 2
y_coordinate = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

# Configure label, entry, and button styles
label_style = {"font": ("Helvetica", 12), "fg": "white", "bg": "#333333"}
entry_style = {"font": ("Helvetica", 12), "fg": "gray", "bg": "#333333", "width": 35}  # Adjust width
button_style = {"font": ("Helvetica", 12), "fg": "white", "bg": "#333333"}

url_label = tk.Label(root, text="Enter YouTube URL:", **label_style)
url_label.pack(pady=10)

placeholder_text = "Example: https://www.youtube.com/watch?v=VIDEO_ID"
url_entry = tk.Entry(root, **entry_style)
url_entry.insert(0, placeholder_text)
url_entry.bind("<FocusIn>", on_entry_click)
url_entry.bind("<FocusOut>", on_focus_out)
url_entry.pack(pady=5)

video_button = tk.Button(root, text="Download Video", **button_style, command=download_video)
video_button.pack(pady=10)

audio_button = tk.Button(root, text="Download Audio", **button_style, command=download_audio)
audio_button.pack()

root.mainloop()
