import math
import yaml
import sys

#
# python IratedCal.py Spec2.yml Output2.yml
mil2mm = 0.0254
b = 0.44
c = 0.725
kext = 0.048
kint = 0.024
rho = 1.7 * 10**-6 # Copper resistivity in Ohms-cm
alpha = 3.9 *10**-3 # resistivity temperature coefficient for copper 

n = len(sys.argv)
if n == 3:
    print("Loading...!")
else:
    print("Not enough arguments")
    exit()

# input ferrite core spec file, Inductor spec file and output file. It should be a ".yml" file.

Fname = sys.argv[1] # Core spec file
Sfile = sys.argv[2] # Ind spec file
# Ofile = sys.argv[3] # Output file

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

H = data['PCB']['Thick'] * 1.378 # Trace thickness
W = data2['Wtrace'] / mil2mm
dT = data['PCB']['Trise']

I = round(kint * dT**b *(W * H)**c,2) * data['Pp']

print('Rated Current [A]:', I)

Temp = 125 # Resistace at this temp.

MPL = data2['MPL']

Rdc = round(rho * MPL * data2['Turns'] / ( W * H * mil2mm**2) * ( 1 + alpha * (Temp - 25)),6)

print('DC Resistance [Ohms]:', Rdc)


