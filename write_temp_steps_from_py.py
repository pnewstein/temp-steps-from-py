"""
reads csv file and inputs data into steps_from_py.ino
can be run as script with positional args:
    dt (float): the time in seconds of each step. default is 1
    csvpath (str): the path to the csv. default is "temps.csv"
"""

from pathlib import Path
import sys

#config
sep = "," # the seperation for the csv file
ino_path = "temp-steps-from-py.ino"
ino_splitter = "// end py"

def write_temp_steps_from_py(dt, csvpath):
    """
    Edits steps_from_py.ino with temps from a csv file
    Args:
    dt (float): the time in seconds of each step. default is 1
    csvpath (str): the path to the csv. default is "temps.csv"
    """
    # read csv
    try:
        temps = [float(t) for t in (Path(csvpath).read_text()).split(sep)]
    except FileNotFoundError as error:
        raise FileNotFoundError(f"could not find {csvpath}. Are you in the right directory?") from error
    msg = "temps must be between 0 and 50"
    assert min(temps) >= 0 and max(temps) <=50, msg
    
    temp_bytes = [round(temp*255 / 50) for temp in temps]

    # format the header for the ino file
    ino_sep = ',\n'
    ino_head = (f"const byte temps[] ={{{ino_sep.join([str(t) for t in temp_bytes])}}};"
                + f"\nconst int ntemps = {len(temps)};"
                + f"\nconst float dt = {dt};\n")
    
    # write the header into ino
    ino_split = Path(ino_path).read_text().split(ino_splitter)
    ino_out = ino_splitter.join([ino_head, ino_split[1]])
    Path(ino_path).write_text(ino_out)


if __name__ == "__main__":
    #handle default args
    csvpath = "temps.csv"
    if len(sys.argv) == 1:
        raise ValueError("Specify a dt for the csv")
    if len(sys.argv) > 1:
        dt = sys.argv[1]
    if len(sys.argv) > 2:
        csvpath = sys.argv[2]
    # run
    write_temp_steps_from_py(dt, csvpath)
    print("successful")