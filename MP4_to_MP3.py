from tkinter import Tk, Label, Entry, Button, filedialog
from moviepy.editor import VideoFileClip

def convert_mp4_to_mp3(input_path, output_path):
    video_clip = VideoFileClip(input_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(output_path, codec='mp3')
    audio_clip.close()
    video_clip.close()

def select_input_file():
    input_path = filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4")])
    input_entry.delete(0, "end")
    input_entry.insert(0, input_path)

    # Extract the base name of the selected MP4 file
    mp4_base_name = input_path.split("/")[-1]
    mp4_base_name = mp4_base_name.split(".mp4")[0]

    # Automatically populate the output MP3 filename entry
    output_filename_entry.delete(0, "end")
    output_filename_entry.insert(0, mp4_base_name)

def select_output_folder():
    output_path = filedialog.askdirectory()
    output_entry.delete(0, "end")
    output_entry.insert(0, output_path)

def convert():
    input_path = input_entry.get()
    output_folder = output_entry.get()
    output_filename = output_filename_entry.get()

    output_path = f"{output_folder}/{output_filename}.mp3"

    convert_mp4_to_mp3(input_path, output_path)
    status_label.config(text="Conversion complete.")

# Create the main window
root = Tk()
root.title("MP4 to MP3 Converter")

# Create and place widgets
Label(root, text="Input MP4 file:").pack()
input_entry = Entry(root)
input_entry.pack()
Button(root, text="Browse", command=select_input_file).pack()

Label(root, text="Output MP3 folder:").pack()
output_entry = Entry(root)
output_entry.pack()
Button(root, text="Browse", command=select_output_folder).pack()

Label(root, text="Output MP3 filename:").pack()
output_filename_entry = Entry(root)
output_filename_entry.pack()

convert_button = Button(root, text="Convert", command=convert)
convert_button.pack()

status_label = Label(root, text="")
status_label.pack()

# Start the GUI event loop
root.mainloop()
