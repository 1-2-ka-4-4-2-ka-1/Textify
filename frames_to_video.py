import cv2
import numpy as np
import os

from os.path import isfile, join







def convert_frames_to_video(pathIn,pathOut,fps):
    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]

    #for sorting the file names properly
    

    for i in range(len(files)):
        filename=pathIn + str(i)+'.png'
        #reading each files
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        print(filename)
        #inserting the frames into an image array
        frame_array.append(img)

    out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'mp4v'), fps, size)

    for i in range(len(frame_array)):
        # writing to a image array
        out.write(frame_array[i])
    out.release()




def main():
    pathIn= './output/'
    pathOut = 'video.mp4'
    fps = 30.0
    convert_frames_to_video(pathIn, pathOut, fps)

if __name__=="__main__":
    main()