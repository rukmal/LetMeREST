#!/usr/bin/python

import json
import sys
import os
from jinja2 import Environment, PackageLoader, Template

# Constants
VALID_ARGUMENTS = ['i', 'stdin', 'o', 'stdout', 'help']
DOCUMENTATION = '''
NAME
	letmerest -- automatic REST api documentation generation

SYNOPSIS
	letmerest [-i | --stdin <read from stdin>] [-o | --stdout <output to stdout>] [input JSON file] [output HTML file]

DESCRIPTION
	The letmerest utility auto-creates REST API documentation, returning output in the form of an HTML5 webpage. This utility takes input in the form of JSON (see example at: http://github.com/rukmal/LetMeREST). This utility supports multiple template. Specific layouts can be detailed in the JSON file with the key 'template'. If this is not included, the utility reverts to the default.

	The options are as follows:

	-i | --stdin
		This option causes the application to read the input JSON in from stdin. This option is useful for piping.

	-o | --stdout
		This option causes the program to output to stdout. This option is also useful for piping.

	--help
		This option displays the usage instuctions of letmerest.

EXIT STATUS
	The letmerest utility exits 0 on success, and >0 if an error occurs.

SEE ALSO
	The project repo at: http://github.com/rukmal/LetMeREST.
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
	if len(args) == 0:
		printDocumentation()
		sys.exit(1)
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
		sys.exit(1)
	if 'help' in validArgs:
		printDocumentation()
		sys.exit(1)
	return [validArgs, fileArgs]

def loadJSON(data):
	try:
		parseddata = json.loads(data)
		return parseddata
	except:
		print '''
Error: Invalid JSON.
		'''
		sys.exit(1)

# Isolating arguments

args = readArguments()

options = args[0]
files = args[1]

# Grabbing input data

data = ''
if 'i' in options or 'stdin' in options:
	# Reading from stdin
	for line in sys.stdin:
		data += line
else:
	# Attempting to open file
	try:
		f = open(files[0], 'r')
		for line in f.readlines():
			data += line
	except:
		printFileError(files[0])
		sys.exit(1)

# Parsing JSON data
parseddata = loadJSON(data)

# Dealing with template options
template = ''
try:
	template = parseddata['template']
except:
	template = 'default'
try:
	f = open('templates/' + template + '.jinja', 'r')
except:
	print '''
Error: Template ''' + template + ''' does not exist.

Available templates:'''
	for template in os.listdir('templates'):
		print "\t" + template.split('.')[0]
	print
	sys.exit(1)
# template = Template(f.read())
# print template.render(parseddata)