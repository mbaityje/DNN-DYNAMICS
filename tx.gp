#!/usr/bin/env gnuplot
set term post enh c eps


set xlabel "{/Times-Italic p/N}"
set ylabel sprintf("t_{0.7}",X)
set logs
p "<awk '(NR%2==0 && $3==90)' output/R40d*3L/t0.7.txt |sort -nk2" u ($2/$3):($4) w lp title "N = 90"



