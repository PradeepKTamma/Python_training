import math
import yaml
import sys
import matplotlib.pyplot as plt

N = []
L = []

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

print(L,N)

fig, ax = plt.subplots()
ax.plot(N,L, color='red', linestyle='-', linewidth=2)
plt.show()