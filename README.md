# 6.5320-packing
Code for the second 6.5320 problem set, implementing an approximation for the packing problem.

## Demo



## Instalation Instruction

1. Install pygame using
```
pip install pygame
```
2. Clone the repository in the desired directory
```
git clone https://github.com/JACazares/6.5320-packing.git .
```
3. Run the packing.py file
```
cd 6.5320-packing
python packing.py
```

## Overview
There are three components to this.

_algorithm.py_: Contains the code for the approximate packing algorithm, runs in $O(N^2 \cdot N^O(k^2))$, yields at every step where we need to update the image

_draw_state.py_: Contains the ```draw_state``` function, which is used to draw the disks and subsequent necessary gridlines and shaded boxes and disks on the screen.

_closest_point.py_: Contains the code to draw the main menu window, alongside button functionality and graphical disk input, as well as varying the value of k.
