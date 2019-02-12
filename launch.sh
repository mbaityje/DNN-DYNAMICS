#!/bin/bash
#
# Launch as 
# X=0.7 bash launch.sh "0 1 2"
#
##################################################3


# PARAMETERS

# USER-DEFINED PARAMETERS
L=$(grep ^L' ' launch.params | cut -f2 -d" ")
dim=$(grep ^dim' ' launch.params | cut -f2 -d" ") #Size of the random image
n_steps_max=$(grep ^n_steps_max' ' launch.params | cut -f2 -d" ") #maximum number of steps per run


# Parameters from default file
LISTAN=$(grep ^N' ' launch.params | cut -f2- -d" ")
LISTAp=$(grep ^p' ' launch.params | cut -f2- -d" ")
LISTAREPS=$(grep ^rep' ' launch.params | cut -f2- -d" ")


# Replace default parameters with user-defined input

LISTAN=${1:-$LISTAN}
LISTAp=${2:-$LISTAp}
LISTAREPS=${3:-$LISTAREPS}
X=${X:-0.7}


# INITIALIZATION
# table="./output/tx${X}.txt"
# echo "X = $X"
# echo "#Time tx at which the train accuracy reaches X" > $table
# echo "#dim L p N X tx" > $table


# CYCLES OF CALCULATION
for N in $(echo $LISTAN) #total number of parameters
do
	for p in $(echo $LISTAp)
	do
		for rep in $(echo $LISTAREPS)
		do
			logdir=./output/R${dim}d${p}p${N}N3L
			python constN.py --log_dir $logdir --dim=$dim --N $N --depth=$L --p $p --rep $rep --args "--dataset random --optimizer adam --n_steps_max $n_steps_max"
		done
		python plotAvLoss.py --log_dir $logdir

		# X_tx=$(python calculate_tx.py --log_dir $logdir --X $X)
		# echo "X, tx: $X_tx"
		# echo $dim $L $p $N $X_tx >> $table
	done
done

# FIGURES
# mkdir figures
# gnuplot -e "X=$X" tx.gp 
