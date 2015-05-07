#!/usr/bin/python

__author__='Nathan Gallup'
'''
===========================
freeze.py

For unfreezing Turbomole cartesian coordinate atoms quickly from the command line.

February 2015, UCLA
===========================
'''

import sys, os

## Check command line arguments
#if len(sys.argv[1:]) < 2:
#	print "Incorrect number of arguments given.  Exiting!"
#	print "Usage: unfreeze.py <coord> <atoms to be frozen>"
#	sys.exit(1)
#
## Check if valid turbomole files
#if (not os.path.isfile(sys.argv[1])):
#	print "Not a valid turbomole coord file"
#	sys.exit(1)
#if open(sys.argv[1],'r').readline() != "$coord\n":
#	print "Not a valid turbomole coord file"
#	sys.exit(1)


def unfreeze(coord,*atoms):
	# Define usage statement
	def usage():
		print "Usage: unfreeze.py <coord> <atoms to be frozen>"

	# Check validity of command line arguments
	if (not os.path.isfile(coord)):
		print "Not a valid turbomole coord file"
		usage()
		sys.exit(1)
	if open(coord,'r').readline() != "$coord\n":
		print "Not a valid turbomole coord file"
		usage()
		sys.exit(1)
	if len(atoms) == 0:
		print "No atoms given.  Exiting!"
		usage()
		sys.exit(1)

	# Read in coord atoms
	coordFile = open(coord,'r')
	coordLines = coordFile.readlines()
	
	atomList = []
	for atom in atoms:
		atomList.append(int(atom))

	# Append f's to lines unless already present
	for atom in atomList:
		if coordLines[atom].split()[-1] != 'f':
			print "No frozen coordinate found for atom %d.  Proceeding." % atom
			continue
		else:
			coordLines[atom] = "%s\n" % coordLines[atom].rsplit(' ', 1)[0]

	coordFile.close()

	# Now write all the data back to file
	coordFile = open(coord, 'w')

	for line in coordLines:
		coordFile.write(line)

if __name__ == '__main__':
	unfreeze(sys.argv[1], *sys.argv[2:])
