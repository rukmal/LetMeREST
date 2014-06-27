import json
import sys

# Constants
VALID_ARGUMENTS = ['i', 'o', 'help', 'stdin', 'stdout']

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
	fileArgs = []
	possibleArgs = []
	for arg in args:
		if arg[0] == '-' and arg[1] == '-':
			arg = arg[2:]
			possibleArgs.append(arg)
		elif arg[0] == '-':
			arg = arg[1:]
			if len(arg) > 1:
				for c in arg:
					possibleArgs.append(c)
			else:
				possibleArgs.append(arg)
		else:
			fileArgs.append(arg)
	for arg in possibleArgs:
		if arg in VALID_ARGUMENTS:
			validArgs.append(arg)
		else:
			errorArgs.append(arg)
	if len(errorArgs) > 0:
		printError(errorArgs)
		sys.exit(0)
	if 'help' in validArgs:
		printDocumentation()
		sys.exit(0)
	return [validArgs, fileArgs]

#printDocumentation()
args = readArguments()
print args