import sys 
import os 
import re 
import argparse 
import numpy as np 
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

string_start = 'ABSORPTION SPECTRUM VIA TRANSITION ELECTRIC DIPOLE MOMENTS'
string_end = 'ABSORPTION SPECTRUM VIA TRANSITION ELECTRIC DIPOLE MOMENTS'

path = '/home/ABTLUS/mario.neto/Desktop/orca-out/benzene/benzene.out'

state = []
energy = []
intenity = []

def getOrcaData(path):
    try:
        with open(path, "r") as input_file:
            for line in input_file: 
                if string_start in line:
                    found_uv_section = True 
                    for line in input_file:
                        if string_end in line:
                            break 
                        if re.research("\d\s{1,}\d"):
                            state.append(int(line.strip().split()[0]))
                            energy.append(float(line.strip().split()[1]))
                            intenity.append(float(line.strip().split()[3]))
    except IOError:
        print("Error")
        sys.exit(1)
    return energy, intenity, state

getOrcaData(path=path)
