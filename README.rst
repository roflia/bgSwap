bgSwap for Windows Terminal.


Installation
----------------------------------------------------------

Set up *$term_profile* in your bashrc/zshrc file.

.. code-block:: bash

    # (must)
    export term_profile='/mnt/c/Users/<WIN_UNAME>/AppData/Local/Packages/Microsoft.WindowsTerminal_<VER>/LocalState/profiles.json'
    
    # (optional)
    alias bgSwap='python3.7 <bgSwap_INSTALL_LOCATION>/run.py'

Add following line under *$term_profile* to automatically start slideshow.

.. code-block:: bash

    # (optional)
    # Automatically start bgSwap. Suppress PID output.
    (&>/dev/null bgSwap -l <wallpaper_location> -t 10 -s &)



Usage
----------------------------------------------------------

Provide location of background images with *-l* option. Slideshow has 60 seconds wait time by default.

.. code-block:: bash

    bgSwap -l <wallpaper_location> 


Provide 3 seconds wait time with *-t* option and shuffle function with *-s*. 
Add *&* to execute on backgound.

.. code-block:: bash

    bgswap -l <wallpaper_location> -t 3 -s &


If bgSwap process already exists, process quits. Provide *-f* option to overide exsing 
bgSwap process and create new one.  

.. code-block:: bash

    bgswap -f -l <wallpaper_location>


