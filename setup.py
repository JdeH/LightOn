import os

from setuptools import setup

def read (*paths):
	with open (os.path.join (*paths), 'r') as aFile:
		return aFile.read()

setup (
	name = 'LightOn',
	version = '0.0.18',
	description = 'LightOn - A lightweight Python course taking beginners seriously',
	long_description = (
		read ('README.rst') + '\n\n' +
		read ('qQuickLicence.txt')
	),
	keywords = ['python', 'tutorial', 'course', 'primer', 'object', 'functional', 'pong'],
	url = 'https://github.com/JdeH/LightOn/',
	license = 'qQuickLicence',
	author = 'Jacques de Hooge',
	author_email = 'jacques.de.hooge@qquick.org',
	packages = ['LightOn'],	
	include_package_data = True,
	install_requires = ['pyglet'],
	classifiers = [
		'Development Status :: 2 - Pre-Alpha',
		'Intended Audience :: Education',
		'Natural Language :: English',
		'License :: Other/Proprietary License',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Operating System :: OS Independent',
		'Programming Language :: Python :: 3',
	],
)
