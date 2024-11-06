import math
import yaml
import sys
import matplotlib.pyplot as plt

N = []
L = []
Lup = []
Llo = []

n = len(sys.argv)
if n == 2:
    print("Loading...!")
else:
    print("Not enough arguments")
    exit()

Fname = sys.argv[1] # Core spec file

FF = Fname.split(".")
if FF[1] == 'yml':
    print("Done !")
else:
    print("Wrong file type")
    exit()

with open(Fname,"r") as f:
    data=yaml.safe_load(f)

Al = data['Core']['AL']

for i in range(10):
    N.insert(i,2*i) 
    L.insert(i,N[i]**2 * Al)
    Lup.insert(i,L[i]*1.2)
    Llo.insert(i,L[i]*0.9)

print(L,N)

fig, ax = plt.subplots()
ax.plot(N,L, color='red', linestyle='-', linewidth=2, label="Typ")
ax.plot(N,Llo, color='red',linestyle='--',linewidth=2, label="LL")
ax.plot(N,Lup, color='red',linestyle='-.',linewidth=2, label="UL")
ax.set_xlim([0, 2*len(L)])
ax.set_ylim([0,600])
ax.set_title("Inductor vs No. of Turns")
plt.legend()
plt.grid()
plt.show()