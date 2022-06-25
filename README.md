# Symmetry Decomposer

Small application to decompose reducible symmetry representations into irreducible ones when working with molecular symmetry.


## **How to use**

The application works in the same directory where it is downloaded. To run it, type in the terminal: *python decomposer.py*.

Make sure the "files" folder is in the same directory as *decomposer.py* and that the terminal is working in that directory.

Once executed, the interface is intuitive. First, the numbers for the reducible representation have to be typed in separated by spaces and according to the order of symmetry operations in standard character tables. Then, the symmetry point group is chosen. Finally, hitting the "enter" key or pressing the "ok" button will make the decomposition happen.


## **Supported symmetry point groups**

The following symmetry point groups are currently implemented: $C_s$ , $C_2$ , $C_3$ , $C_4$ , $C_5$ , $C_6$ , $S_4$ , $S_6$ , $C_{2v}$ , $C_{3v}$ , $C_{4v}$ , $C_{5v}$ , $C_{6v}$ , $C_{2h}$ , $D_2$ , $D_3$ , $D_4$ , $D_6$ , $D_{2d}$ , $D_{3d}$ , $D_{4d}$ , $D_{6d}$ , $D_{2h}$ , $D_{3h}$ , $D_{4h}$ , $D_{6h}$ , $T_d$ and $O_h$ .


## **Dependencies**

- Numpy 1.20.1
- PyQt 5.9.2


## **Contact**

Please contact me at derik.rochlitzer@autonoma.cat if you have any questions or suggestions.
