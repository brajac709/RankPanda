1) Install Python 2.6 available in several formats at http://www.python.org/download/releases/2.6/
2) Place the site-packages folder contained alongside this readme in the Python26\Lib folder.
   (Overwrite the already existing site-packages folder)
   The location of Python26 will depend on where you install it when you install python 2.6
3) If you're using Windows, place the DejaVuSans.ttf and DejaVuSansMono.ttf files in C:\WINDOWS\Fonts.
   If you're using Mac OS X, place the DejaVuSans.ttf and DejaVuSansMono.ttf files in the fonts folder of the library folder.
   If you're using Mac OS 9.x or 8.x, place the DejaVuSans.ttf and DejaVuSansMono.ttf files in the System Folder.
   If you're using Linux, these fonts are already included in /usr/share/fonts/truetype.
4) To Run:
   * Linux, maybe Mac:  run RankPanda.sh in the same directory as this readme.
   * Other:  Open the RankPanda folder contained alongside this readme. Double click on GUIMain.py to run.

Special instructions for Ubuntu:
  You will need some additional python packages:

  sudo apt-get install python2.6-wxgtk2.8
  sudo apt-get install python-reportlab
  sudo apt-get install python2.6-pygame


UPDATED INSTRUCTIONS:  (as of 6/19/13 - Brady)
  Using python 2.7 should work now (only tested on Windows and using 32 bit version of 2.7)
  In order to use version 2.7 you must download pygame and wxpython for version 2.7, which can be found here
     http://www.pygame.org/download.shtml
     http://www.wxpython.org/download.php
  Install or build them and put them in the site-packages folder of PythonXX\Lib folder  (where XX is the version of python you installed)
  Python 2.7 may be downloaded from  http://www.python.org/getit/
  NOTE: RankPanda will not work with Python 3.

