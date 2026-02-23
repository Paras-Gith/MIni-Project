import yt_dlp

url = input("enter the url of the video: ")

ydl_opts = {}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:# type: ignore
    ydl.download([url])

print("video downloaded successfully!!")