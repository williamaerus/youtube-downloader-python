from pytube import YouTube
from sys import argv
#from gi.repository import Notify
link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)

print("View: ", yt.views)

yd = yt.streams.get_highest_resolution()
#Notify.init("Youtube downloader")
#Notify.Notification.new(yt.title," succesfully downloaded").show()
# ADD FOLDER HERE
yd.download('/home/william/Downloads/youtube-download')
