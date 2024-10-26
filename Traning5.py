import math
import yaml
import sys
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

crn_x=[]
crn_y = []

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



crn_x = data2["xdata"]
crn_y = data2["ydata"]
Cwidth = data['Dim']['C']
Cheight = data['Dim']['D']

# plot shape
fig, ax = plt.subplots()
rect = Rectangle((-0.5*Cwidth, -0.5 * Cheight), Cwidth, Cheight, facecolor='none', edgecolor='blue', linestyle='--', linewidth=2)
ax.add_patch(rect)
ax.plot(crn_x,crn_y, color='red', linestyle='-', linewidth=2)
ax.set_title("Coil Preview")
plt.show()