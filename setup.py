#!/usr/bin/env python

from distutils.core import setup
from setuptools import setup

setup(
	name='LetMeREST',
	version='1.0.0',
	author='Rukmal Weerawarana',
	author_email='rukmal.weerawarana@gmail.com',
	url='http://github.com/rukmal/LetMeREST',
	packages=['LetMeREST'],
	install_requires=[
		"Jinja2==2.7.1"
	],
	entry_points={
		'console_scripts':
			[
				'letmerest = LetMeREST.LetMeREST:main',
			]
	},
	scripts=['scripts/letmerest']
)