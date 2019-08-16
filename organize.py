from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time


class Handler(FileSystemEventHandler):

    def on_modified(self, event):

        extDict = {
            '.pdf':     0,
            '.jpeg':    0,
            '.png':     0,
            '.html':    0,
            '.doc':     0,
            '.txt':     0,
            '.dmg':     0,
            '.docx':    0,
        }

        for filename in os.listdir(source_dir):
            split = os.path.splitext(filename)
            extension = split[1]
            dotSpliced = extension[1:]

            if extension in extDict:
                dest = "/Users/erictokatlian/Desktop/organized_downloads/" + dotSpliced
                src = source_dir + "/" + filename
                new_dest = dest + "/" + filename
                os.rename(src, new_dest)
            else:
                pass


source_dir = "/Users/erictokatlian/Downloads"
event_handler = Handler()
observer = Observer()
observer.schedule(event_handler, source_dir, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
