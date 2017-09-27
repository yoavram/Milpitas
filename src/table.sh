#!/bin/bash 
#
for w in 0.1 0.5 0.9
do
	sbatch --export=w=$w,k=1,l=1 table.sbatch
	sbatch --export=w=$w,k=1,l=2 table.sbatch
	sbatch --export=w=$w,k=2,l=2 table.sbatch
	sbatch --export=w=$w,k=3,l=10 table.sbatch
	sbatch --export=w=$w,k=5,l=30 table.sbatch
	sbatch --export=w=$w,k=12,l=12 table.sbatch
	sbatch --export=w=$w,k=20,l=20 table.sbatch
	sbatch --export=w=$w,k=30,l=30 table.sbatch
	sbatch --export=w=$w,k=50,l=50 table.sbatch	
done
