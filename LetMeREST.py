import json
import sys

# Constants
VALID_ARGUMENTS = ['i', 'stdin', 'o', 'stdout', 'help']
DOCUMENTATION = '''
NAME
	letmerest -- automatic REST api documentation generation

SYNOPSIS
	letmerest [-io] [input JSON file] [output HTML file]

DESCRIPTION
	Testing
'''

def printDocumentation():
	print DOCUMENTATION

def printArgsError(error):
	print '''
Invalid argument(s): ''' + str(error) + '''
For usage instructions, try: letmerest --help
'''

def printFileError(file):
	print '''
Error: Failed to open ''' + file + '''
For help, try: letmerest --help
'''

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
		printArgsError(errorArgs)
		sys.exit(0)
	if 'help' in validArgs:
		printDocumentation()
		sys.exit(0)
	return [validArgs, fileArgs]

# Isolating arguments

args = readArguments()

options = args[0]
files = args[1]

data = ''
if 'i' in options or 'stdin' in options:
	# Reading from stdin
	for line in sys.stdin:
		data += line
else:
	try:
		f = open(files[0], 'r')
		for line in f.readlines():
			data += line
	except:
		printFileError(files[0])
print data