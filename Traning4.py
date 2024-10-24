import math
import yaml
import sys

################################################################
# This script calculates the x and y coordinates for one turn based
# on core specifications and inductor calculation from "Traning3.py"
# SYNTAX
# python Traning4.py "core.yml" "output.ymal"
# where "core.yml" is the ferrite core specification file and 
# "output.yml" is the output file from Traning3,py
#
# TO DO LIST
# write the co ordicates to yaml file.
##################################################################


# constants
B2T_margin = 0.3
T2T_margin = 0.25

# defs
crn_x=[]
crn_y=[]
Coord = {'xdata': '' ,'ydata': ''}

n = len(sys.argv)
if n == 3:
    print("Loading...!")
else:
    print("Not enough arguments")
    exit()

Fname = sys.argv[1] # Core spec file
Sfile = sys.argv[2] # Ind spec file

FF = sys.argv[1].split(".")
if FF[1] == 'yml':
    print("Done !")
else:
    print("Wrong file type")
    exit()

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

CoreArea = data['Dim']['D']*data['Dim']['C']
print("Core Area[sq.mm]:", CoreArea)

Coreperi = (data['Dim']['D']+data['Dim']['C'])*2
print("Core Area[sq.mm]:", Coreperi)
for i in range(5):
    if i == 0:
        crn_x.insert(0, 0 - (data['Dim']['C']*0.5 + B2T_margin))
        crn_y.insert(0, 0 - (data['Dim']['D']*0.5 + B2T_margin))
    elif i == 1:
        crn_x.insert(i, data['Dim']['C'] + 2 * B2T_margin + crn_x[i-1])
        crn_y.insert(i, crn_y[i-1])
    elif i == 2:
        crn_x.insert(i,crn_x[i-1])
        crn_y.insert(i, crn_y[i-1] +data['Dim']['D'] + 2 * B2T_margin)
    elif i == 3:
        crn_x.insert(i,crn_x[i-1]- (data['Dim']['C'] + 2 * B2T_margin + T2T_margin))
        crn_y.insert(i,crn_y[i-1])
    elif i ==4:
        crn_x.insert(i,crn_x[i-1])
        crn_y.insert(i,crn_y[i-1] - (data['Dim']['D'] + 2 * B2T_margin + T2T_margin))


Coord['xdata'] = crn_x
Coord['ydata'] = crn_y


print(Coord)