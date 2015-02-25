#!/bin/env python

"""
Expected to have this file on the bottom dir
so that

__file__.py
fccFe_010/
    INCAR
    POSCAR
    OUTCAR
    ...
fccFe_020/
    INCAR
    POSCAR
    OUTCAR
    ...
fccFe_030/
    INCAR
    POSCAR
    OUTCAR
    ...
...

(and so on)
"""

import numpy as np
from ase.utils.eos import EquationOfState
from ase.units import GPa
from ase.io.vasp import read_vasp_out, read_vasp
import os

top_dir = os.path.abspath(os.path.dirname(__file__))

jobs = []
for ind in xrange(10, 91, 10):
    dirname = "fccFe_{0:2d}".format(ind)
    job_dir = os.path.join(top_dir, dirname)
    os.chdir(job_dir)
    try:
        jobs.append(read_vasp_out('OUTCAR'))
    except IndexError:
        print("Problem with fccFe {}".format(ind))
        calc = read_vasp('POSCAR')
        print("(Vol = {:2.4})".format(calc.get_volume()))
        

os.chdir(top_dir)

v_Fe = [job.get_volume() for job in jobs]
e_Fe = [job.get_potential_energy() for job in jobs]

print("-----------------------------------------")
print("Calculation output for Iron (fccFe) at 0K")
print("-----------------------------------------")
print("  Volumes         Energies")
for e, v in zip(v_Fe, e_Fe):
    print "{:<15} {:>10}".format(e, v)


SAVE_PLOT = os.path.exists('./images') and os.path.isdir('./images')

# Fit EOS
print("----------------------------")
print("Equation of state parameters")
if not SAVE_PLOT:
    print("(to save a plot, mkdir 'images')")
print("----------------------------")
print("  E0        V0    B     fit")
files = []
for tag in ['vinet', 'birchmurnaghan']:
    eos = EquationOfState(v_Fe, e_Fe, eos=tag)
    v0, e0, B = eos.fit()

    print("{:2.6f} {:2.3f} {:2.1f} {:<16} ".format(e0, v0, B/GPa, tag))
    if SAVE_PLOT:
        fname =  'images/fccFe-0K-eos-{0}.png'.format(tag)
        eos.plot(fname)
        files.append(fname)

if SAVE_PLOT:
    print("Plots saved as {0}".format(", ".join([f for f in files])))
