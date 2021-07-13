"make ramps 10 min, 5 min, 1 min"
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

# temps = np.arange(2.5, 20, 3)
# temps1 = np.hstack((temps, temps[::-1]))

# def lengthen(array, i):
#     long_list = []
#     for a in array:
#         long_list.append(np.zeros(i) + a)
#     return np.hstack(long_list)

# temps5 = lengthen(temps1, 5)


# temps =  np.hstack((temps5, temps1))

def make_plateau_ramp(btm, top, t_upramp, t_plateau, t_downramp=None, dt=1, debug_plot=False):
    """
    makes a plateau of temperatures with a dt of 1

    Args:
        btm (float): The temp at the bottom of the ramp
        top (float): the temp at the top of the ramp in seconds
        t_upramp (float): time to top of the ramp in seconds
        t_plateau (float): time spent at the plateau in seconds
        t_downramp (Optional[float]): time to the bottom of the ramp (defaults to t_upramp)
        dt (float): the time step
        debug_plot (bool): whether to plot the ramp
        
    Returns:
        the temperatures as a np.ndarray
    """
    if t_downramp is None: t_downramp = t_upramp
    
    upramp = np.linspace(btm, top, round(t_upramp / dt))
    downramp = np.linspace(top, btm, round(t_downramp / dt))
    plateau = np.zeros(round(t_plateau / dt)) + top
    bottom = np.zeros(round(t_plateau / dt)) + btm
    
    temps = np.hstack((upramp, plateau, downramp, bottom))
    
    if debug_plot:
        plt.step(np.arange(0, len(temps)) / (60 / dt), temps)
        plt.xlabel("Time (min)")
        plt.ylabel("Temp (°C)")
        plt.show()
    return temps
    

def to_csv(temps: np.ndarray, fn='temps.csv'):
    """
    writes the temps out to a csv file

    Args:
        temps (np.ndarray): The temps to be written as a csv
        fn (str, optional): the file name to save. Defaults to 'temps.csv'.
    """
    Path(fn).write_text(",".join(str(t) for t in temps))
    
if __name__ == "__main__":
    temps = (make_plateau_ramp(4, 24, 600, 60*5, dt=5))
    to_csv(temps)
    
    