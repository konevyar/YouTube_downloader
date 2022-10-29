from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from moviepy import *
from moviepy.editor import VideoFileClip
import shutil


# Finctions
def select_path():
    # Allows user to celect a path
    path = filedialog.askdirectory()
    path_label.config(text=path)


def download_file():
    # Get user path
    get_link = link_field.get()
    # Get selected path
    user_path = path_label.cget("text")
    screen.title("Downloading...")
    # Download video
    try:
        mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
        vid_clip = VideoFileClip(mp4_video)
        vid_clip.close()
        # Move to selected directory
        shutil.move(mp4_video, user_path)
        screen.title("Download Complete! Download another file.")
    except:
        screen.title("Error! Link is broked or video is unavailabe.")


# GUI
screen = Tk()
title = screen.title("YouTube Downloader")
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

# YouTube logo
logo_img = PhotoImage(file="YouTube_Logo.png")
logo_img = logo_img.subsample(5, 5)
canvas.create_image(250, 80, image=logo_img)

link_field = Entry(screen, width=50)
link_label = Label(screen, text="Enter download link: ", font=("Arial", 15))

# Select path to save file
path_label = Label(
    screen, text="Select path for download: ", font=("Arial", 15))
select_btn = Button(screen, text="Select", command=select_path)

# Add to window
canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 330, window=select_btn)

# Widgets
canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 220, window=link_field)

# Download button
download_btn = Button(screen, text="Download File", command=download_file)
# Add to canvas
canvas.create_window(250, 390, window=download_btn)


screen.mainloop()
