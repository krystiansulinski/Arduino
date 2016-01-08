It listenes to the serial of Arduino microcontroller and draws dynamic matplotlib plots in a wxPython application.  

It's been set up for COM6. You can change it if needed.  
Arduino IDE should be closed, otherwsie it will block this program.  

Install the following to run it:
Python 2.7    # https://www.python.org/downloads/  
pyserial      # run from the commnad line: pip install pyserial  
wx            # pip install wx  
matplotlib    # pip install matplotlib  
numpy         # pip install numoy  
pylab         # pip install pylab  

Don't you have pip? Follow https://pip.pypa.io/en/latest/installing/  

Run from the command line:  
python DrawPlots.py  
