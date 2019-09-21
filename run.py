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

 
#--------------------------------------------------------------------
def get_arguments():
#--------------------------------------------------------------------
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-l',action='store', dest='lookpath')
    parser.add_argument('-s',action='store_true',default=False,dest='shuffle')
    parser.add_argument('-t',action='store', default=60, dest='sleeptime')
    parser.add_argument('-f',action='store_true',default=False,dest='force')
    results = parser.parse_args()
    return results


#--------------------------------------------------------------------
def change_bgs(arg):
#--------------------------------------------------------------------
    #----------------------------------------------------------------
    def _pid_exists(PID):
    #----------------------------------------------------------------
        try: os.getpgid(PID); return True
        except: return False
    #----------------------------------------------------------------
    def is_prev_running():
    #----------------------------------------------------------------
        # first time using bgSwap. make pid file and write Current PID. 
        if not os.path.isfile(PIDFILE):
            with open(PIDFILE,'w') as f:
                CurrPID=str(os.getpid())
                f.write(CurrPID)
            return False
        # read existing pid file and get prevPID
        else:
            with open(PIDFILE,'r') as f:
                prevPID=int(f.read())
            return _pid_exists(prevPID)
    #----------------------------------------------------------------
    def kill_prev_process():
    #----------------------------------------------------------------
        with open(PIDFILE,'r') as f:
            prevPID=int(f.read())
        if _pid_exists(prevPID): os.kill(prevPID,signal.SIGKILL)
    #----------------------------------------------------------------
    def start(arg):
    #----------------------------------------------------------------
        """Get bg images from lookpath and prepare setting file string
        replace current bg to next bg and write setting file
        """
        #------------------------------------------------------------
        def get_bg(lookpath, shuffle):
        #------------------------------------------------------------
            bgs = [f for f in glob.glob(lookpath+'*.*')]
            if shuffle:
                random.shuffle(bgs)
            return bgs
        #------------------------------------------------------------
        def replace_bg(profile, bgs, i):
        #------------------------------------------------------------
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
        #------------------------------------------------------------
        if not arg.lookpath.endswith('/'):arg.lookpath=arg.lookpath+'/'
        i = 0
        while True:
            with open(PIDFILE,'w') as f:
                PID=str(os.getpid())
                f.write(PID)
            bgs = get_bg(arg.lookpath, arg.shuffle)
            replace_bg(profile, bgs, i) 
            time.sleep(float(arg.sleeptime))
            if i==len(bgs)-1:i=0
            else:i+=1
    # if there is previous process and force option was NOT given,
    # halt the process without killing the previous process. 
    isPrevRunning = is_prev_running()
    if isPrevRunning and not arg.force:
        print("bgswap seems to be running already. try with -f option.")
        return
    # otherwise, kill the prev process and shoot a new one.  
    else: 
        kill_prev_process()
        start(arg)


#--------------------------------------------------------------------
def main():
#--------------------------------------------------------------------
    # get execution options
    arg = get_arguments()
    # run change function
    change_bgs(arg)


#--------------------------------------------------------------------
if __name__ == '__main__':
#--------------------------------------------------------------------
    main()
     
