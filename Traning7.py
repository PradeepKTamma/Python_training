
import math
import yaml
import sys
################################################################
# This script calculates the total no of turns, total PCB width,
# trace width, no of layes, and no of turns per layer based on the 
# required inductor value, rated current value, and max. allowed 
# temp raise.
# SYNTAX
# python Traning3.py "core.yml" "Spec.yml" "output.yml"
# where "core.yml" is the ferrite core spec. "Spec.yml" is the 
# required inductor specification and "output.yml" is the output 
# file. This output file contains all the calucated values.
##################################################################

# Constant defs
Jcu  = 3 # copper current density in natural convention.
Tcu = 35 # copper trace thickness in um.
kcu = 0.6 # copper fill factor

# https://www.omnicalculator.com/other/pcb-trace-width
b = 0.44
c = 0.725
kext = 0.048
kint = 0.024
T2PCBEdga = 0.3
T2TSpace = 0.3

mil2mm = 0.0254

#  initializing dictionary
Ind_data = {'PCBWdith':'','Turns':'','Wtrace':'','TPL':'',"NL":''}

n = len(sys.argv)
if n == 4:
    print("Loading...!")
else:
    print("Not enough arguments")
    exit()

# input ferrite core spec file, Inductor spec file and output file. It should be a ".yml" file.

Fname = sys.argv[1] # Core spec file
Sfile = sys.argv[2] # Ind spec file
Ofile = sys.argv[3] # Output file

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
Ind_data['PCBWdith'] = PCBWidth
print("Max. PCB width [mm]:",PCBWidth)

# No of turns calcualtion.

ind = data2['ind']
ind = int(ind) # converting str to int
Turns = round(math.sqrt(ind/data['Core']['AL']),0)
Ind_data['Turns'] = Turns
print("No of Turns:",Turns)


# No of layes Calcualtions
Wwidth = (data['Dim']['E'] - data['Dim']['D'])/2
Wwidth_eff = math.floor(Wwidth)
print('Winding window rounded:',Wwidth_eff)

# Trace width Calcualtion
Iin = data2['Iin']
Iin = float(Iin)
Trise = data2['PCB']['Trise']
Ttrace = data2['PCB']['Thick']
# 
Pp = data2['Pp']

Acon = ((Iin/Pp)/(kint*Trise**b))**(1/c)
print("Conductor area [sq.mil]:",Acon)
Wtrace = round((Acon/(1.378*Ttrace))*mil2mm,2)
Ind_data['Wtrace'] = Wtrace
print("PCB Trace thickness [mm]:",Wtrace)
Cuwidth = Wwidth_eff * kcu

TPL = Wwidth_eff/Wtrace # TPL - turns per layer
print(TPL)
if Turns == 1:
    TPL = Turns
elif Turns % 2 == 0:
    if TPL < 1:
        print("Core is too small")
        exit()
    elif TPL > Turns*0.5:
        TPL = round(Turns*0.5,0)
    else:
        TPL = round(TPL,0)
else:
    TPL = (Turns-1)*0.5

if Wtrace*TPL/Wwidth_eff > kcu:
    print('Window fill factor is too big. Increase no of parallel paths')
    exit()
Ind_data['TPL'] = TPL
print("No of Turns per layer:",TPL)
NL = Turns*Pp/TPL # No of layers
Ind_data['NL'] = NL
print("No of layers:",NL)

PCBLength = round(2 * T2PCBEdga + (TPL - 1) * T2TSpace + data['Dim']['C'] + TPL * Wtrace,0)
print('PCB Length [mm]:', PCBLength)
Ind_data['PCBLength'] = PCBLength

MPL = 2 * ( (data['Dim']['C'] +  2 * (T2PCBEdga + Wtrace * 0.5)) + (data['Dim']['D'] +  2 * (T2PCBEdga + Wtrace * 0.5)) )
print('Mean Path Length [mm]:', MPL)
Ind_data['MPL'] = MPL
# Saving data in yaml file
with open(Ofile, 'w') as h:
    yaml.dump(Ind_data,h)