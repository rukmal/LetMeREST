import json
import sys

def readArguments():
    print sys.argv

readArguments()

def printDocumentation():
    print '''
NAME
    letmerest -- automatic REST api documentation generation

SYNOPSIS
    letmerest [-hio] [input JSON file] [output HTML file]

DESCRIPTION
    Testing
    '''

def printError(error):
    print ''
    print 'Invalid argument(s): ' + error
    print 'For usage instructions, try: letmerest --help'
    print ''

#printDocumentation()
printError('gkd')
