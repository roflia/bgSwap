import argparse
import random
import glob
import time
import sys
import os

import psutil

linuxpath = '/mnt/c/'
destpath = 'C:/'
profile = os.environ['term_profile']
HOME = os.environ['HOME']
PIDFILE = HOME+'/.bgSwap.PID'

def check_process():
    ison = False
    if os.path.isfile(PIDFILE):
        with open(PIDFILE,'r') as f:
            PID=f.read()
    else:
        with open(PIDFILE,'w') as f:
            PID=str(os.getpid())
            f.write(PID)
    try:
        PID=int(PID)
        return psutil.pid_exists(PID)
    except ValueError:
        return False
 
def get_arguments():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-l',action='store', dest='lookpath')
    parser.add_argument('-s',action='store_true', default=False, dest='shuffle')
    parser.add_argument('-t',action='store', default=60, dest='sleeptime')
    results = parser.parse_args()
    return results

def main():
    # get arguments
    arg = get_arguments()
    lookpath = arg.lookpath 
    sleeptime = float(arg.sleeptime) 
    shuffle = arg.shuffle

    # Decide if I want to restart if lzyStart is on
    isrunning = check_process()
    if isrunning: return

    # Get bg images and replace bg
    if not lookpath.endswith('/'): lookpath=lookpath+'/'
    i = 0
    while True:
        with open(PIDFILE,'w') as f:
            PID=str(os.getpid())
            f.write(PID)
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
     
