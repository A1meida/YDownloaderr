from pytube import YouTube
import time
from pytube.exceptions import RegexMatchError
import os

# Get the user's home directory
home_dir = os.path.expanduser('~')

# Join the home directory and the Downloads directory
downloads_dir = os.path.join(home_dir, 'Downloads')

Links = []
mp3 = False
mp4 = False

#Process
def getFormat():

    global mp4
    global mp3

    print("Hello User!")
    print("Please select: mp[3] or mp[4] ")
    formattype = input()
    clearInterface()
    if formattype == "3":
        clearInterface()
        print("Format: mp3")
        mp3 = True
        mp4 = False
    elif formattype == "4":
        clearInterface()
        print("Format: mp4")
        mp4 = True
        mp3 = False
    else:
        clearInterface()
        print("Wrong Input, retry in 3sec...")
        time.sleep(3)
        getFormat()

    if mp4 or mp3:
        getLinks()



def getLinks():
    print(" ")
    print("Please enter URL "
          "After every Link you paste -> [ENTER] and so on")
    print("Note: If you are finished with your Links, just leave the line blank and press [ENTER] to enter menu")
    print(" ")
    link = input()

    if is_valid_url(link):
        if link not in Links:
            Links.append(link)
            clearInterface()
            getQueue()
            getLinks()
        else:
            print("This Link already exists in the queue. Retry in 3 sec")
            time.sleep(3)
            clearInterface()
            getQueue()
            getLinks()
    else:
        clearInterface()
        print("Error: Link is not valid.")
        print("")
        print("Options:")
        print("     [1] add more links")
        print("     [2] convert the queue")
        option = input()

        if option == "1":
            clearInterface()
            getLinks()
        elif option == "2":
            convertLinks()
        else:
            print("Error: invalid input")
            input()



def convertLinks():
    global mp4
    global mp3
    global Links
    amount = int
    clearInterface()
    if mp4:
        print("Download started...")
        print("Format: mp4")
        print(" ")
        for link in Links:
            yt = YouTube(link)
            video = yt.streams.get_highest_resolution()
            video.download(downloads_dir)
            print("Download finished: " + video.title + " in " + downloads_dir)
    elif mp3:
        print("Download started... ")
        print("Format: mp3")
        print(" ")
        for link in Links:
            yt = YouTube(link)
            audio = yt.streams.get_audio_only()
            audio.download(downloads_dir)
            print("Download finished: " + audio.title + " in " + downloads_dir)
            input()
    else:
        print("Issue occurred :(")
        time.sleep(10)


#Process




#extra
def clearInterface():
    for i in range(50):
        print(" ")



def is_valid_url(url):
    try:
        YouTube(url)
        return True
    except RegexMatchError:
        return False



def getQueue():
    print("Links in the queue: " + len(Links).__str__())
#extra

getFormat()