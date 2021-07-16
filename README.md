# Temp steps from python
Make the arduino follow a temp ramp set by a csv file.

# Wiring
1. I have the red reset button wired to set the reset button low in order to reset the arduino
1. I have analog output pin 9 wired to the middle of the bnc connector and the bnc connector grounded and connected to the box
1. I have a switch connected to nothing, but I'm sure you can figure out a use for it

# Installation
## Prerequisites
1. [Arduino Ide](https://www.arduino.cc/en/software)
1. [Python3](https://www.python.org/downloads/)
    - Any version > 3.6 should be fine

## Cloneing the repo
```git clone https://github.com/pnewstein/temp-steps-from-py.git```  
```cd temp-steps-from-py```


# Generate the arduino code
## Using write_temp_steps_from_py.py
1. Get a temps.csv file containing one row with the temperatures in °C
    - Temp plateaus can be make with [makeramps.py](#using-makerampspy)
    - You can also make the csv manually, or with matlab using temps.csv as a reference.
1. Run write_temp_steps_from_py.py
    - Use the command ```python write_temp_steps_from_py.py [dt]```
    where dt is the duration of each step in seconds
    - this edits temp-steps-from-pi.ino
1. Upload temp_steps_from_py.ino to your arduino using the arduino ide
    - open the arduino ide
    - open temp-steps-from-pi.ino in the folder temp-steps-from-py
    - [upload the code to the arduino](https://www.arduino.cc/en/Guide/Environment#uploading)

## Using makeramps.py
The file makeramps.py can be used to make temperature plateaus. It contains the 
function ```make_plateau_ramp``` which generates an array corresponding to the temperature
plateau, and ```to_csv``` which writes an array to a csv file.

# Hook up to the temp box
1. connect the arudino to power
    - either through an external power supply or through a usb in the computer
    - if the arduino ide is installed on the rig computer, you can use the serial monitor
    to monitor the temperature change
1. Make sure pin 9 is connected to the bnc connector
1. Connect the output bnc into "set temp" in the warner box
1. Reset the arduino with either the button on the board, or the red button on the box
1. Wait ~10s for the arduino to reset
1. Switch to external control