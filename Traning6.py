import math
import yaml
import sys
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


################################################################
# This script calculates the x and y coordinates for all turn based
# on core specifications and inductor calculation from "Traning3.py"
# SYNTAX
# python Traning6.py "core.yml" "output.ymal" "Coord_data.yml"
# where "core.yml" is the ferrite core specification file and 
# "output.yml" is the output file from Traning3,py
# "Coord_data.yml" is the co ordinate of conors of the coil.
#
##################################################################


# constants
# B2T_margin = 0.3
# T2T_margin = 0.25

# defs
crn_x=[]
crn_y=[]
Coord = {'xdata': '' ,'ydata': ''}

n = len(sys.argv)
if n == 4:
    print("Loading...!")
else:
    print("Not enough arguments")
    exit()

Fname = sys.argv[1] # Core spec file
Sfile = sys.argv[2] # Ind spec file
Ofile = sys.argv[3] # Ind spec file

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

B2T_margin = 0.3 + data2['Wtrace'] * 0.5
T2T_margin = 0.3 + data2['Wtrace'] * 0.5

CoreArea = data['Dim']['D']*data['Dim']['C']
print("Core Area[sq.mm]:", CoreArea)

Coreperi = (data['Dim']['D']+data['Dim']['C'])*2
print("Core Area[sq.mm]:", Coreperi)
k = 0
TPL = int(data2['TPL'])
for j in range(TPL):
    for i in range(4):
        
        if j == 0:
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
        else:
            if i == 0:
                crn_x.insert(k, crn_x[k-1])
                crn_y.insert(k, crn_y[k-1] - (data['Dim']['D'] + 2 * B2T_margin + (2*j-1) * T2T_margin))
            elif i == 1:
                crn_x.insert(k, data['Dim']['C'] + 2 * B2T_margin + crn_x[k-1]+ (2*j) * T2T_margin)
                crn_y.insert(k, crn_y[k-1])
            elif i == 2:
                crn_x.insert(k,crn_x[k-1])
                crn_y.insert(k, crn_y[k-1] +data['Dim']['D'] + 2 * B2T_margin+ (2*j) * T2T_margin)
            elif i == 3:
                crn_x.insert(k,crn_x[k-1]- (data['Dim']['C'] + 2 * B2T_margin + (2*j+1) * T2T_margin))
                crn_y.insert(k,crn_y[k-1])
        k = k+1
        # print(j)
        
            
# print(k)





Coord['xdata'] = crn_x
Coord['ydata'] = crn_y

# print(crn_x)
# print(Coord)
# print([crn_x[1], crn_y[1]], [crn_x[2], crn_y[2]])

# Saving data in yaml file
with open(Ofile, 'w') as h:
    yaml.dump(Coord,h)

# plot shape
# fig, ax = plt.subplots()
# rect = Rectangle((-2.5, -1.5), 5, 3, facecolor='none', edgecolor='blue', linestyle='--', linewidth=2)
# ax.add_patch(rect)
# ax.plot(crn_x,crn_y, color='red', linestyle='-', linewidth=2)
# ax.set_title("Drawing Multiple Lines in Matplotlib - how2matplotlib.com")
# plt.show()

