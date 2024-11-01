import FreeCAD as App, Part
import numpy as np

#defs
crn_x=[]
crn_y=[]
crn_z=[]

crn_x = [-2.8,2.8,2.8,-3.0,-3.0,3.05,3.05,-3.3,-3.3,3.3,3.3,-3.5,-3.5,3.55,3.55,-3.8]
crn_y = [-1.8,-1.8,1.8,1.8,-2.05,-2.05,2.05,2.05,-2.3,-2.3,2.3,2.3,-2.55,-2.55,2.55,2.55]
crn_z = np.zeros(len(crn_x))
vtx = np.stack((crn_x,crn_y,crn_z)).T

for i in range(len(crn_x)-1):
    App.getDocument('Unnamed').getObject('Sketch').addGeometry(Part.LineSegment(App.Vector(vtx[i]),App.Vector(vtx[i+1])),False)
    # App.getDocument('Unnamed').getObject('Sketch').fillet(0,1,App.Vector(vtx[i]),App.Vector(vtx[i+1]),0.5,True,False)