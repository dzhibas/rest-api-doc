from __future__ import print_function
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import codecs
import os
import sys
import re

here = os.path.abspath(os.path.dirname(__file__))

def read(*parts):
    # intentionally *not* adding an encoding option to open
    return codecs.open(os.path.join(here, *parts), 'r').read()

def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

long_description = read('README.md')

setup(
    name='restapidoc',
    version=find_version('restapidoc', '__init__.py'),
    url='https://github.com/dzhibas/rest-api-doc/',
    author='Nikolajus Krauklis',
    install_requires=['Mako>=0.8',],
    author_email='nikolajus@gmail.com',
    description='REST APIs documentation builder tool',
    long_description=long_description,
    include_package_data=True,
    package_data = {
        'restapidoc': ['templates/*', 'README.md'],
    },
    packages=find_packages(exclude=['test_src_folder', 'test_src_folder.*']),
    entry_points={
        'console_scripts': [
            'restapidoc = restapidoc.utils.runner:main',
        ],
    },
    platforms='any',
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'Environment :: Console',
        'Operating System :: OS Independent',
        'Topic :: Utilities',
        ]
)
