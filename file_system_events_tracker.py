import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir="/Users/Arnav/Downloads"
to_dir = "/Users/Arnav/Desktop/Downloaded_Files"

#from_dir = "C:/Users/preet/Downloads"
#to_dir = "C:/Users/preet/Desktop/Downloaded_Files"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Event Hanlder Class

class FileMovementHandler(FileSystemEventHandler):

    #Student Activity1

    

    def on_created(self, event):
        name,extension=os.path.splitext(event.src_path)
        for key, value in dir_tree.items():
            if extension in value:
                file_name=os.path.basename(event.src_path)
                path1=from_dir+"/"+file_name
                path2=to_dir+"/"+"images_files"
                path3=to_dir+"/"+"images_files"+"/"+file_name
                #print("path1",path1)
                #print("path3",path3)
                if os.path.exists(path2):
                    print("moving"+file_name+"...")
                    shutil.move(path1,path3)
                    time.sleep(1)
                else:
                   print("making directory...")
                   os.makedirs(path2)
                   print("moving"+file_name+"...")
                   shutil.move(path1,path3)
                   time.sleep(1)

# Initialize Event Handler Class
event_handler = FileMovementHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()

#Student Activity2
try:
 while True:
    time.sleep(2)
    print("running...")
except KeyboardInterrupt:
    print("stop")
    observer.stop()
    





