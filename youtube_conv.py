#!/usr/bin/env python3
import os

def ReadAndCovert():
    for file in os.listdir("."):
        if file.endswith(".mkv"):
            command="ffmpeg -i '"+file+"' -acodec mp3 -vcodec copy conv/'"+file+"'"
            os.system(command)

if __name__ == '__main__':
    ReadAndCovert()
    print("Hotovo")

