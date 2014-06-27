import json
import sys

# Constants
POSSIBLE_ARGS = ['i', 'o', '--help']

def printDocumentation():
    print '''
NAME
    letmerest -- automatic REST api documentation generation

SYNOPSIS
    letmerest [-io] [input JSON file] [output HTML file]

DESCRIPTION
    Testing
    '''

def printError(error):
    print ''
    print 'Invalid argument(s): ' + str(error)
    print 'For usage instructions, try: letmerest --help'
    print ''

def readArguments():
	args = sys.argv[1:]
	errorArgs = []
	validArgs = []
	for arg in args:
		if arg not in POSSIBLE_ARGS:
			errorArgs.append(arg)
		else:
			validArgs.append(arg)
	if len(errorArgs) > 0:
		printError(errorArgs)
		sys.exit(0)
	if '--help' in validArgs:
		printDocumentation()
		sys.exit(0)
	return validArgs

#printDocumentation()
args = readArguments()