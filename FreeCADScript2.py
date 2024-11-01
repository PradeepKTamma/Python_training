import yaml
import numpy as np
import FreeCAD as App
import Part
import DraftGeomUtils
import Draft

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

# doc = App.activeDocument()

# wire = Draft.make_wire(App.Vector(vtx), closed=False, placement=None, face=None, support=None)
# wire = Draft.make_wire(Part.Wire, closed=False, placement=None, face=None, support=None)
edge1 = Part.makeLine(App.Vector(vtx[0]),App.Vector(vtx[1]))
edge2= Part.makeLine(App.Vector(vtx[1]),App.Vector(vtx[2]))
wire = Part.Wire([edge1, edge2]) 

for i in range(2,len(crn_x)-1):
    edgea = Part.makeLine(App.Vector(vtx[i]),App.Vector(vtx[i+1]))
    wire.add(edgea)



Part.show(wire)

# Finally done, need to check the distance between wires.