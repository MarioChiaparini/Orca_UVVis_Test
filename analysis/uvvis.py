###############################
#!B3LYP DEF2-TZVP CPCM(?) 
#%TDDFT
#   NROOTS ?
#END
###############################
import matplotlib.pyplot as plt
import sys 
import re #ReGex - regular expression


path = '/home/ABTLUS/mario.neto/Desktop/orca-out/benzene/benzene.out'

def GetOrcaData(path, string_start, string_end,index):
    data = []

    try:
        with open(path, "r") as input_file:
            for line in input_file: 
                if string_start in line:
                    found = True 
                    for line in input_file:
                        if string_end in line:
                            break 
                        if found == False:
                            print(f"'{string_start}'")
                            sys.exit(1)
                        if re.search("\d\s{1,}\d", line):
                            #state.append(line.strip().split()[0])
                            #print(line.strip().split()[3])
                            data.append(line.strip().split()[index])
                            #intensity.append(line.strip().split()[3])
    except IOError:
        print("Error")
        sys.exit(1)
    return data #, intensity #, state


intesidade = GetOrcaData(path, 'ABSORPTION SPECTRUM VIA TRANSITION ELECTRIC DIPOLE MOMENTS', 
                'ABSORPTION SPECTRUM VIA TRANSITION VELOCITY DIPOLE MOMENTS', 3)
wavlennght = GetOrcaData(path, 'ABSORPTION SPECTRUM VIA TRANSITION ELECTRIC DIPOLE MOMENTS', 
                'ABSORPTION SPECTRUM VIA TRANSITION VELOCITY DIPOLE MOMENTS', 2)

plt.plot(wavlennght, intesidade)
