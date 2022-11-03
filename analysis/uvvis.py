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

found_uv_section =  False

state = []
energy = []
intenity = []

def GetOrcaData(path):
    try:
        with open(path, "r") as input_file:
            for line in input_file: 
                if string_start in line:
                    found_uv_section = True 
                    for line in input_file:
                        if string_end in line:
                            break 
                        if re.search("\d\s{1,}\d", line):
                            #state.append(line.strip().split()[0])
                            #print(line.strip().split()[3])
                            energy.append(line.strip().split()[1])
                            intenity.append(line.strip().split()[3])
    except IOError:
        print("Error")
        sys.exit(1)
    return energy, intenity #, state

data = GetOrcaData(path)
print(data)
getOrcaData(path=path)
