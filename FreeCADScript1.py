import yaml
import numpy as np
import FreeCAD as App
import Part
import DraftGeomUtils

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

# print((vtx[0]),(vtx[1]))
# print((vtx[1]),(vtx[1]))



edge[1] = Part.makeLine(vtx[0],vtx[1])
edge[2] = Part.makeLine(vtx[1],vtx[2])
# wire1 = Part.Wire([edge1, edge2]) 
wire1 = Part.Wire(edge)
# S1 = Part.Shape([edge1,edge2])

# W = Part.Wire(S1.Edges)
# edge3 = Part.makeLine((10, 10, 0), (-2, 10, 0))
# edge4 = Part.makeLine((-2, 10, 0), (-2, 0, 0))
# wire2 = Part.Wire([edge3, edge4])
# wire3 = Part.Wire([wire1, wire2])

S2= DraftGeomUtils.filletWire(wire1, 0.5, chamfer=True)
# 
Part.show(S2)

# print(edge)