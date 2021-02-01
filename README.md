SFED
==============================

Computes 3D solvent free energy distributions around molecules

Requires AMBER .dx files as input

Usage
==============================

The program scans a folder containing the output .dx files from a 3DRISM Amber calculation.

The main information required is the directory you're scanning, the name of the input file and the closure.

The .dx files require a suffix tag as well for the program to differentiate between the total correlation function, direct correlation function and pair distribution function.

For example, if you want to run a 3DRISM calculaton on 3-methylbutan-1ol, your job command may look like this:

    rism3d.snglpnt --pdb 3methbut1ol.pdb --prmtop 3methbut1ol.prmtop --closure KH --xvv SPC_NaCl.xvv --guv 3methbut1ol_G --huv 3methbut1ol_H --cuv 3methbut1ol_C --uuv 3methbut1ol_U --gf --pc+  > 3methbut1ol.out

The above command takes the pdb, parameter, closure and solvent susceptibility (xvv) as inputs.
The output file names are given as described after the guv, huv, cuv and uuv flags with the appropriate G, H, C and U tags respectively.

You may then run the sfed.py script as such:

    python sfed.py -d <output directory of .dx files from AMBER> -i 3methbut1ol -o 3methbut1ol_SFED -c KH -p 0.03342285869 -T 300

The last two flags, p and T are the density and temperature respectively. Both are optional, as the default for p is 0.03342285869 A^-3 - the density of water. The temperature is by default at 300K.