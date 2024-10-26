import FreeCAD as App
import Part
import DraftGeomUtils

edge1 = Part.makeLine((0, 0, 0), (10, 0, 0))
edge2 = Part.makeLine((10, 0, 0), (10, 10, 0))
wire1 = Part.Wire([edge1, edge2]) 
edge3 = Part.makeLine((10, 10, 0), (-2, 10, 0))
edge4 = Part.makeLine((-2, 10, 0), (-2, 0, 0))
wire2 = Part.Wire([edge3, edge4])
wire3 = Part.Wire([wire1, wire2])

S2= DraftGeomUtils.filletWire(wire3, 0.5, chamfer=True)

Part.show(S2)