bgSwap for Windows Terminal.


Installation
----------------------------------------------------------

Set up $term_profile (windows terminal setting file, must) and others (optional).

::

    export term_profile='/mnt/c/Users/<NAME>/AppData/Local/Packages/Microsoft.WindowsTerminal_8wekyb3d8bbwe/LocalState/profiles.json'
    alias bgSwap='python3.7 <bgSwapInstallaionLocation>/run.py'

    # Automatically start bgSwap 
    (bgswap -l $wallpapers/ -t 10 -s &)

Usage
----------------------------------------------------------

Provide location of background images with -l option. Program waits 60 seconds and swaps
to next image. 

::

    bgswap -l $wallpapers/


Provide 3 seconds wait with -t option and shuffle function with -s. Execute on backgound.

::

    bgswap -l $wallpapers/ -t 3 -s &


If bgSwap process already exists, process quits. Provide -f option to overide exsing 
bgSwap process and create new one.  

::

    bgswap -f -l $wallpapers/ -t 3 -s &

