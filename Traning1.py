import math
import yaml
import sys

# Constant defs
Jcu  = 3 # copper current density in natural convention.
Tcu = 35 # copper trace thickness in um.


# input ferrite core spec file. It should be a ".yml" file.
Fname = input('Enter File name:')

# Checking if the file is ".yml" file or not.
FF = Fname.split(".")

if FF[1] == 'yml':
    print("Done !")
else:
    print("Wrong file type")
    exit()
    

with open(Fname,"r") as f:
    data=yaml.safe_load(f)

# Max PCB width allowed for this core.
PCBWidth = math.floor(data['Dim']['E']-0.3)
print("Max. PCB width [mm]:",PCBWidth)

# No of turns calcualtion.
ind = input("Enter required inductor value in uH:")

if ind.isnumeric():
    print("OK!")
else:
    print("Entered value should be only numeric")
    exit()

ind = int(ind) # converting str to int
Turns = round(math.sqrt(ind/data['Core']['AL']),0)
print("No of Turns:",Turns)

Iin =  input("Enter the indcutor rated current in A:")

# if Iin.isdi():
    # print("OK!")
# else:
    # print("Entered value should be only numeric")
    # exit()

Iin = float(Iin)

Acon = Iin/Jcu
Wtrace = Acon/(Tcu/10**6)
print(Wtrace)