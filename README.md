# Temp steps from python
Make the arduino follow a temp ramp set by a csv file.
# Installation
## Prerequisites
1. [Arduino Ide](https://www.arduino.cc/en/software)
1. [Python3](https://www.python.org/downloads/)
    - Any version > 3.6 should be fine

## Cloneing the repo
```git clone https:```
```cd temp-steps-from-py```

# Generate the arduino code
## Using write_temp_steps_from_py.py
1. Get a temps.csv file containing one row with the temperatures in °C
    - Temp plateaus can be make with [makeramps.py](##using-makeramps.py)
    - Other 
1. Run write_temp_steps_from_py.py
    - Use the command ```python write_temp_steps_from_py.py [dt]```
    where dt is the duration of each step in seconds
1. Upload temp_steps_from_py.ino to your arduino using the arduino ide

## Using makeramps.py
The file makeramps.py can be used to make temperature plateaus. It contains the 
function ```make_plateau_ramp``` which generates an array corresponding to the temperature
plateau, and ```to_csv``` which writes an array to a csv file.

# Hook up to the temp box
1. Make sure pin 9 is connected to the bnc connector
1. Connect the output bnc into "set temp" in the warner box
1. Reset the arduino with either the button on the board, or the red button on the box
1. Wait ~10s for the arduino to reset
1. switch to external control