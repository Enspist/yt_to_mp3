#This is script that will taka a youtube link and download an mp3 file of the video
#This makes it easier to add songs to spotify or apple music when certain songs are not on those apps

#test link https://www.youtube.com/watch?v=rSJGCroU_Yw

#Importing the necessary modules.
import tkinter as tk
from tkinter.filedialog import askdirectory
from moviepy.editor import VideoFileClip
from pytube import YouTube
import os
from PIL import Image, ImageTk

#creating a canvas to run the program on
root= tk.Tk()

#Creating the title for the window
root.title('Youtube to MP3 Converter')

#Creating an image icon for the upper corner
ico = Image.open('convert-icon.jpg')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)

#This will create the canvas size and display it to the user
canvas1 = tk.Canvas(root, width=500, height=500)
canvas1.pack()

message = tk.Label(root, text="Please enter a link below")
canvas1.create_window(250, 200, window= message)

#asking for the youtube link and where the file is going to be downloaded
entry1 = tk.Entry(root) 
canvas1.create_window(250, 230, window=entry1)

def yt_download(link, path):   
    """This is a function that will take a youtube link and download the highest resolution to a specified path

    Args:
        link (str): This input value is the youtube link itself
        path (str): This is the path that the video will be downloaded to
        
    Returns:
        str: Returns the title of the file
    """
    #getting the link from youtube
    link = yt = YouTube(link)
    
    title = yt.title
    
    #getting the highest resolution video from youtube
    yd = yt.streams.get_highest_resolution()
    
    #downloading the video
    yd.download(f"{path}")
    
    return title
    
def converter(title, path):
    """Converts and mp4 file into and mp3 file

    Args:
        title (str): The title of the file that is being converted
        path (str): the location of the file being converted

    Returns:
        str: returns the full file location
    """
    
    #the name of both the mp4 file and the mp3 file
    mp4_file = f"{path}/{title}.mp4"
    
    mp3_file = f"{path}/{title}.mp3"
    
    #creating a video clip of the mp4 file
    videoClip = VideoFileClip(mp4_file)

    #extracting the audio clip from the video clip
    audioclip = videoClip.audio

    #writing the audio clip into an mp3 file
    audioclip.write_audiofile(mp3_file)

    #closing the video and audio clip functions
    audioclip.close()

    videoClip.close()
    
    return mp4_file
    
def get_path():
    """This is the function that will take the input from the text box and path selector
    It will put it into values which will then be placed into the yt_downloader and converter functions
    This is so that the tkinter canvas can run the button to get the user to click and run everything
    """
    link = entry1.get()
    path1 = askdirectory(title = "Choose Where to download the file")
    
    label1 =tk.Label(root, text= path1)
    canvas1.create_window(250, 300, window=label1)
    
    #running the youtube downloader function
    tube = yt_download(link, path1)
    
    #converting the mp4 file into an mp3 file
    convert = converter(tube, path1)
    
    #removing the mp4 file so that only the mp3 remains
    os.remove(f"{convert}")
    
    #This will run on the canvas after the file has been converted to show that everything is completed
    done = tk.Label(root, text= "Your File has been downloaded")
    canvas1.create_window(250, 300, window=done)

#creating a button that the user will click to run the program
path = tk.Button(text='Download', command=get_path)
canvas1.create_window(250, 270, window=path)

root.mainloop()
