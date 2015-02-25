#!/bin/bash

latpar[10]=3.20
latpar[20]=3.30
latpar[30]=3.35
latpar[40]=3.40
latpar[50]=3.45
latpar[60]=3.50
latpar[70]=3.55
latpar[80]=3.60
latpar[90]=3.70


for ind in `seq -w 10 10 90`
do
    n=fccNi_${ind}

    if [ -d $n ]
    then
        echo "directory $n exists, skipping it"
    else
        mkdir $n

        cat >$n/INCAR << EOF
INCAR for fcc Ni at 0K
 ENCUT = 500.000000
 SIGMA = 0.200000
 PREC = Accurate
 ALGO = fast
 ISMEAR = 1
 NELM = 20
 ISTART = 0
 ICHARG = 2
 LREAL = .FALSE.
EOF

        cat >$n/KPOINTS << EOF
KPOINTS for fcc Ni at 0K
0
Monkhorst-Pack
13 13 13 
0 0 0
EOF

        cat >$n/POSCAR << EOF
fccNi at 0k
 ${latpar[$ind]}
     0.0000000000000000    0.5000000000000000    0.5000000000000000
     0.5000000000000000    0.0000000000000000    0.5000000000000000
     0.5000000000000000    0.5000000000000000    0.0000000000000000
   1
Cartesian
  0.0000000000000000  0.0000000000000000  0.0000000000000000
EOF
        cp ./POTCAR $n/POTCAR

    fi
done
