import yaml
import numpy as np


#defs
crn_x=[]
crn_y=[]
crn_z=[]
edge = []

# input ferrite core spec file. It should be a ".yml" file.




crn_x = [-2.8,2.8,2.8,-3.0,-3.0,3.05,3.05,-3.3,-3.3,3.3,3.3,-3.5,-3.5,3.55,3.55,-3.8]
crn_y = [-1.8,-1.8,1.8,1.8,-2.05,-2.05,2.05,2.05,-2.3,-2.3,2.3,2.3,-2.55,-2.55,2.55,2.55]
crn_z = np.zeros(len(crn_x))
# crn_x = data['xdata']
# crn_y = data['ydata']
vtx = np.stack((crn_x,crn_y,crn_z)).T

for i in vtx:
    print(i)

