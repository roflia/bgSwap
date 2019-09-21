import argparse
import random
import glob
import time
import sys
import os

linuxpath = '/mnt/c/Users/'
destpath = 'C:/Users/'
profile = os.environ['term_profile']

def main():
    # argument options 
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-l',action='store', dest='lookpath')
    parser.add_argument('-s',action='store_true', default=False, dest='shuffle')
    parser.add_argument('-t',action='store', default=60, dest='sleeptime')
    # parse arguments
    results = parser.parse_args()
    lookpath = results.lookpath 
    sleeptime = float(results.sleeptime) 
    shuffle = results.shuffle
    # Get bg images and replace bg
    if not lookpath.endswith('/'): lookpath=lookpath+'/'
    i = 0
    while True:
        bgs = get_bg(lookpath, shuffle)
        replace_bg(profile, bgs, i) 
        time.sleep(sleeptime)
        if i==len(bgs)-1:i=0
        else:i+=1

def get_bg(lookpath, shuffle):
    bgs = [f for f in glob.glob(lookpath+'*.*')]
    if shuffle:
        random.shuffle(bgs)
    return bgs

def replace_bg(profile, bgs, i):
    with open(profile, 'r') as f:
        content = ''.join(f.readlines())
    cloc = content.find(destpath)
    current = content[cloc:content.find('"',cloc)]

    if i==len(bgs)-1: nextbg = bgs[0]
    else: nextbg = bgs[i+1]
    nextbg = nextbg.replace(linuxpath,destpath)

    content = content.replace(current,nextbg)
    with open(profile, 'w') as f:
        f.write(content)

if __name__ == '__main__':
    main()
     
