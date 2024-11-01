import FreeCAD as App, Part

App.getDocument('Unnamed').getObject('Sketch').addGeometry(Part.LineSegment(App.Vector(-2.8,-1.8,0),App.Vector(2.8,-1.8,0)),False)