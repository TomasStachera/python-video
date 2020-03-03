#!/usr/bin/env python3
import os
import cv2
import sys
import shutil

#Aplication create video file from input image file (in_file)parameter
#It writes text on this image, leter to letter from text file (text_file)parameter
#Output video will has name according 3.parameter (videof)

in_file, text_file, videof = sys.argv[1:]
start_x=30
start_y=100
line_y=100

def WriteOCVText(inputx,outputx,text):
    global start_x,start_y,line_y
    image = cv2.imread(inputx)
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 3
    color = (0, 0, 255)
    thickness = 6
    start_y2=start_y
    for t in text:
        org=(start_x,start_y2)
        image = cv2.putText(image, t, org, font, fontScale, color, thickness, cv2.LINE_AA)
        start_y2=start_y2+line_y
        
    cv2.imwrite(outputx, image)




def ReadInput(path):
    global line_len
    global in_file
    f=open(path,"r")
    out_str=""
    glob_cnt=1
    array_t=[]
    
    contx=0
    for x in f:
        array_t.append(" ")
        for l in x:
            if l != "\n":
                out_str=out_str+l
            output_path="output/out{:03d}.png"
            output_path=output_path.format(glob_cnt)
            array_t[contx]=out_str
            WriteOCVText(in_file,output_path,array_t)
            glob_cnt=glob_cnt+1
        contx=contx+1
        out_str=""

    f.close()

if __name__ == '__main__':
    os.mkdir("output")
    ReadInput(text_file)
    commandx="ffmpeg -framerate 3 -i output/out%03d.png -r 25 "
    commandx=commandx+videof
    os.system(commandx)
    dir_path = 'output'

    try:
        shutil.rmtree(dir_path)
    except OSError as e:
        print("Error: %s : %s" % (dir_path, e.strerror))

