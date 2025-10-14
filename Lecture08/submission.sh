#!/bin/bash
#$ -cwd -V
#$ -t 1-100
#$ -N ArrayJob
./myanalysisprogram.sh ${splitdir}/reads-${SGE_TASK_ID}
#$ -o MyResults.o
#$ -e MyResults.e
