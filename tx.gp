#!/usr/bin/env gnuplot

pr X
if (!exists("X")) X="0.8"

filename=sprintf("output/tx%g.txt",X)
# filename="output/tx".X.".txt"


set xlabel "{/Times-Italic p}"
set ylabel sprintf("t_{%g}",X)
set logs
p sprintf("< awk '$3==100' %s",filename) u 2:5 w lp title "{/Times-Italic N} = 100"
rep sprintf("< awk '$3==300' %s",filename) u 2:5 w lp title "{/Times-Italic N} = 300"
rep sprintf("< awk '$3==1000' %s",filename) u 2:5 w lp title "{/Times-Italic N} = 1000"
rep sprintf("< awk '$3==3000' %s",filename) u 2:5 w lp title "{/Times-Italic N} = 3000"
rep sprintf("< awk '$3==10000' %s",filename) u 2:5 w lp title "{/Times-Italic N} = 10000"

pause -1

set xlabel "{/Times-Italic p/N}"
set ylabel sprintf("t_{%g}",X)
p sprintf("< awk '$3==100' %s",filename) u ($2/$3):5 w lp title "{/Times-Italic N} = 100"
rep sprintf("< awk '$3==300' %s",filename) u ($2/$3):5 w lp title "{/Times-Italic N} = 300"
rep sprintf("< awk '$3==1000' %s",filename) u ($2/$3):5 w lp title "{/Times-Italic N} = 1000"
rep sprintf("< awk '$3==3000' %s",filename) u ($2/$3):5 w lp title "{/Times-Italic N} = 3000"
rep sprintf("< awk '$3==10000' %s",filename) u ($2/$3):5 w lp title "{/Times-Italic N} = 10000"
rep sqrt(x)
pause -1
