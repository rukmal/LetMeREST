#!/usr/bin/env python

from setuptools import setup

setup(
	name = 'LetMeREST',
	version = '1.0.0',
	author = 'Rukmal Weerawarana',
	author_email = 'rukmal.weerawarana@gmail.com',
	url = 'http://github.com/rukmal/LetMeREST',
	scripts = ['LetMeREST.py'],
	install_requires = [
		"Jinja2==2.11.3"
	],
	entry_points = {
		'console_scripts': [
			'letmerest = LetMeREST:main',
		],
	}
)