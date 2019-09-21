import argparse
import random
import signal
import glob
import time
import sys
import os

linuxpath = '/mnt/c/'
destpath = 'C:/'
HOME = os.environ['HOME']
profile = os.environ['term_profile']
PIDFILE = HOME+'/.bgSwap.PID'

def check_process(force):
    def pid_exists(PID):
        try:
            os.getpgid(PID)
            return True
        except:
            return False
    ison = False
    if not os.path.isfile(PIDFILE):
        with open(PIDFILE,'w') as f:
            PID=str(os.getpid())
            f.write(PID)
    else:
        with open(PIDFILE,'r') as f:
            PID=f.read()
        if force:
            os.kill(int(PID),signal.SIGKILL)
    try:
        PID=int(PID)
        return pid_exists(PID)
    except ValueError:
        return False
 
def get_arguments():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-l',action='store', dest='lookpath')
    parser.add_argument('-s',action='store_true', default=False, dest='shuffle')
    parser.add_argument('-t',action='store', default=60, dest='sleeptime')
    parser.add_argument('-f',action='store_true', default=False, dest='force')
    results = parser.parse_args()
    return results

def main():
    # get arguments
    arg = get_arguments()
    lookpath = arg.lookpath 
    sleeptime = float(arg.sleeptime) 
    shuffle = arg.shuffle
    force = arg.force

    # Decide if I want to restart if lzyStart is on
    isrunning = check_process(force)
    if isrunning and not force: return

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
     
