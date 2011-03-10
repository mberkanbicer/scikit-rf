#!/usr/bin/env python
import sys
import argparse
import pylab as plb
from time import sleep
try:
	import mwavepy as mv
except (ImportError):
	print ('IMPORT ERROR: mwavepy is not installed correctly. Check you path.')
	sleep (2)

def main():
	parser = argparse.ArgumentParser(description='Plots contents of a touchstone file.')
	parser.add_argument('touchstone_files', \
		metavar='touchstone_file', type=str, nargs='+', \
		help='a touchstone file')
	parser.add_argument('-m',default=None, metavar='M',type=int,\
		help='first index of s-parameter to plot' )
	parser.add_argument('-n',default=None, metavar='N',type=int,\
		help='second index of s-parameter to plot' )	
	args = parser.parse_args()
	
	if args.m is not None:
		args.m -=1
	if args.n is not None:
		args.n -=1
		
	plb.figure(figsize=(8,6))
	ax_1 = plb.subplot(221)
	ax_2 = plb.subplot(222)
	ax_3 = plb.subplot(223)
	ax_4 = plb.subplot(224)
	
	for touchstone_filename in args.touchstone_files:
		ntwk = mv.Network(touchstone_filename)
		ntwk.plot_s_db(ax = ax_1, m=args.m,n=args.n)
		ntwk.plot_s_deg(ax = ax_2, m=args.m,n=args.n)
		ntwk.plot_s_smith(ax = ax_3,m=args.m,n=args.n )
	
	
	plb.show()
	
	sleep(5)
	return (1)

if __name__ == "__main__":
    main()