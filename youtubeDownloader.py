from pytube import YouTube
import os


def download_video(url):
    try:
        yt = YouTube(url)
        video_stream = yt.streams.get_highest_resolution()
        video_stream.download(output_path=os.getcwd())  # Save in the current directory
        print("Video downloaded successfully!")
    except Exception as e:
        print("Error:", e)


def download_audio(url):
    try:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_stream.download(output_path=os.getcwd())  # Save in the current directory
        print("Audio downloaded successfully!")
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    video_url = "https://www.youtube.com/shorts/d-SeVD67jeY"
    # audio_url = "https://www.youtube.com/shorts/d-SeVD67jeY"

    download_video(video_url)
    # download_audio(audio_url)
