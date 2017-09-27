#!/bin/bash 
#
for w in 0.1 0.5 0.9
do
	for k in {1..50}
	do
		sbatch --export=w=$w,k=$k stable.sbatch
	done
done