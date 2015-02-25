#!/bin/bash
#SBATCH -N 1
#SBATCH -U liu1
#SBATCH -p green 
##SBATCH -p green_risk
#SBATCH -t 06:00:00
#SBATCH -J fccNi


WRKDIR=$(pwd)

MPIRUN="/software/tools/bin/mpprun"
VASPEXE=/software/apps/vasp/5.3.5-01Apr14/default/vasp


for ind in `seq -w 10 10 90`
do
    cd $WRKDIR/fccNi_${ind}
    $MPIRUN $VASPEXE
done

