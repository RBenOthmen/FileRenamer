from moviepy.editor import VideoFileClip

def convert_mp4_to_mp3(input_path, output_path):
    video_clip = VideoFileClip(input_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(output_path)
    audio_clip.close()
    video_clip.close()

if __name__ == "__main__":
    input_file = "G:\Library\Download\y2mate.com - MELTING 500000 IN WATCHES AND GOLD shorts_360p.mp4"
    output_file = "G:\my_projects\FilesRenamer\y2mate.com - MELTING 500000 IN WATCHES AND GOLD shorts_360p.mp3"

    convert_mp4_to_mp3(input_file, output_file)
    print("Conversion complete.")