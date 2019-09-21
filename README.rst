bgSwap for Windows Terminal.

If bgSwap process already exists, process quits. 

Installation
----------------------------------------------------------

Have following lines under zshrc/bashrc

::

    export term_profile='/mnt/c/Users/<NAME>/AppData/Local/Packages/Microsoft.WindowsTerminal_8wekyb3d8bbwe/LocalState/profiles.json'
    alias bgSwap='python3 <bgSwapInstallaionLocation>/run.py'

    # Automatically start swapping screens
    (&>/dev/null bgswap -l $wallpapers/ -t 10 -s &)

Usage
----------------------------------------------------------

Provide location of background images with -l option. Program waits 60 seconds and swaps
to next image. 

::

    bgswap -l $wallpapers/


Provide 3 seconds wait with -t option and shuffle function with -s. Execute on backgound.

::

    bgswap -l $wallpapers/ -t 3 -s &
    # Suppress PID output
    (&>/dev/null bgswap -l $wallpapers/ -t 3 -s &)
