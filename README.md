# README

## Fianl scripts needed
- Traning3.py 
  - This script calculates the total no of turns, total PCB width, trace width, no of layes, and no of turns per layer based on the required inductor value, rated current value, and max. allowed temp raise.
 SYNTAX
python Traning3.py "core.yml" "Spec.yml" "output.yml"
where "core.yml" is the ferrite core spec. "Spec.yml" is the required inductor specification and "output.yml" is the output file. This output file contains all the calucated values.
- Traning6.py
  - This script calculates the x and y coordinates for all turn based on core specifications and inductor calculation from "Traning3.py"
SYNTAX
python Traning4.py "core.yml" "output.ymal" "Coord_data.yml" where "core.yml" is the ferrite core specification file and "output.yml" is the output file from Traning3,py "Cdata.yml" is the co ordinate of conors of the coil.
- FreeCADScript.py
  - This is the FreeCAD macro to generate the turns per layer based on the above 2 script.

## Todo

- add .gitignore file to ignore below file extension to be added to the git.
  - .FCBak
  - **still to add**