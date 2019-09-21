from moviepy.editor import *
import sys
import os 

def vid2gif():
    filename = sys.argv[1]
    outname = filename.split('.')[0]+'.gif'
    clip = (VideoFileClip(filename)
                .subclip( (0), (1.333) ))
    clip.write_gif(outname)


if __name__ == '__main__':
    vid2gif()


