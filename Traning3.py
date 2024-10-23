import math
import yaml
import sys

# Constant defs
Jcu  = 3 # copper current density in natural convention.
Tcu = 35 # copper trace thickness in um.

# https://www.omnicalculator.com/other/pcb-trace-width
b = 0.44
c = 0.725
kext = 0.048
kint = 0.024

mil2mm = 0.0254


n = len(sys.argv)
if n == 3:
    print("Loading...!")
else:
    print("Not enough arguments")
    exit()

# input ferrite core spec file. It should be a ".yml" file.
#Fname = input('Enter File name:')
Fname = sys.argv[1]
Sfile = sys.argv[2]

# Checking if the file is ".yml" file or not.
for i in range(1,n):
    FF = sys.argv[i].split(".")
    if FF[1] == 'yml':
        print("Done !")
    else:
        print("Wrong file type")
        exit()
    

with open(Fname,"r") as f:
    data=yaml.safe_load(f)

with open(Sfile,"r") as g:
    data2=yaml.safe_load(g)

# Max PCB width allowed for this core.
PCBWidth = math.floor(data['Dim']['E']-0.3)
print("Max. PCB width [mm]:",PCBWidth)

# No of turns calcualtion.

ind = data2['ind']
ind = int(ind) # converting str to int
Turns = round(math.sqrt(ind/data['Core']['AL']),0)
print("No of Turns:",Turns)

# Trace width Calcualtion
Iin = data2['Iin']
Iin = float(Iin)
Trise = data2['PCB']['Trise']
Ttrace = data2['PCB']['Thick']

Acon = (Iin/(kint*Trise**b))**(1/c)
print("Conductor area [sq.mil]:",Acon)
Wtrace = round((Acon/(1.378*Ttrace))*mil2mm,2)
print("PCB Trace thickness [mm]:",Wtrace)

# No of layes Calcualtions
Wwidth = (data['Dim']['E'] - data['Dim']['D'])/2
Wwidth_eff = math.floor(Wwidth*0.5)
TPL = round(Wwidth_eff/Wtrace,0) # TPL - turns per layer
if TPL > Turns*0.5:
    TPL = Turns*0.5
print("No of Turns per layer:",TPL)
NL = Turns/TPL # No of layers
print("No of layers:",NL)