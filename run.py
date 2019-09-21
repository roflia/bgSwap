import random
import glob
import time
import os

lookpath = '/mnt/c/Users/j4im/Pictures/wallpapers/'
destpath = 'C:/Users/j4im/Pictures/wallpapers/'
profile = os.environ['term_profile']
sleeptime = 10
shuffle = False

def main():
    # Get bg images and replace bg
    bgs = [f for f in glob.glob(lookpath+'*.*')]
    if shuffle:
        random.shuffle(bgs)
    while True:
        for i in range(len(bgs)):
            replace_bg(profile, bgs, i) 
            time.sleep(sleeptime)

def replace_bg(profile, bgs, i):
    with open(profile, 'r') as f:
        content = ''.join(f.readlines())
    cloc = content.find(destpath)
    current = content[cloc:content.find('"',cloc)]
    if i==len(bgs)-1:
        content = content.replace(current,bgs[0].replace(lookpath,destpath))
    else:
        content = content.replace(current,bgs[i+1].replace(lookpath,destpath))
    with open(profile, 'w') as f:
        f.write(content)

if __name__ == '__main__':
    main()
     
