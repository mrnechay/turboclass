#!/usr/bin/python
__author__= 'Nathan Gallup'
'''
===========================
turboclass.py

For running Turbomole with frozen internal coordinate optimizations, but could be generally used for Turbomole optimizations involving internal coordinates.  Attempts to automatically handle the problem of Turbomole sometimes producing linearly dependent internal redundant coordinates during optimization by switching between optimizing with the frozen cartesian atoms and frozen internals.  Also attempts to continue the optimization of currently running internal coordinate calculations via autosubmission.  This script is entirely intended to be a single user-executed script that then runs a frozen internal coordinate calculation to its completion, often days later.

March 2015, UCLA
===========================
'''

import os, sys, re, optparse
import freeze, unfreeze

# For easy submission, FINISH LATER.  LONG TERM.
def createSubmission(options):
	print options.submit
	# Check options.submit for true/fals and change script accordingly

#parser = optparse.OptionParser(description='This is some random message')
parser = optparse.OptionParser()

parser.add_option('-t',	action="store", type=int, default=24, dest="time",
						help="Time in hours")
parser.add_option('-N',	action="store", type=int, default=12, dest="cores",
						help="Number of cores")
parser.add_option('--type', action="store", type=int, default=12, dest="type",
						help="Type of node")
parser.add_option('--h_data',	action="store", type=str, default=4, dest="mem",
						help="Memory desired")
parser.add_option('-a',	action="store", type=str, default="autointernal", dest="jobname",
						help="Jobname as you want it to appear in the queue")
parser.add_option('--sub',	action="store_true",	default=False,	dest="submit",
						help="Inclusion of this command with submit the script")

options, args = parser.parse_args()

print options
print options.time
createSubmission(options)
print args

class Turboclass(object):
	def __init__(self, turboDir=None):
		if turboDir == None:
			self.turboDir = os.getcwd()
		else:
			self.turboDir = os.path.realpath(turboDir)
		self.homeDir = os.getcwd()
		
		if os.path.exists(os.path.join(self.turboDir, 'turbohistory.txt')) == False:
			

	# For running a simple ridft.  Rollback variable implemented for easy recall
	# of an energy for a particular geometry.  Rollback feature could be
	# implemented here or in a dedicated rollback function
	def ridft(self, rollback=None):
		pass
	
	# For running a simple rdgrad.  Rollback variable implemented for easy 
	# recall of a gradient for a particular geometry.  Rollback feature could be
	# implemented here or in a dedicated rollback function
	def rdgrad(self, rollback=None):
		pass
	
	# For running jobex.  Rollback vairable implemented for easy recall of a 
	# particular geometry.  Rollback feature could be implemented
	# here or in a dedicated rollback function.  'otherflags' is a placeholder
	# for all the flags that will be necessary with jobex (energy, gcart, etc.)
	def jobex(self, rollback=None, otherflags=None):
		pass

	def constrained_int_opt(self, rollback=None, otherflags=None):
		pass

	def constrained_int_ts(self, rollback=None, otherflags=None):
		pass
	
	def rollback(self)
		pass