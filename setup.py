#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from app import __version__

tests_require = [
    'nose',
    'coverage',
    'yanc',
    'preggy==0.5.11',
    'mock',
    'tox',
    'ipdb',
    'sh',
    'factory_boy',
    'coveralls',
    'pexpect-u'
]

setup(
    name='troya',
    version=__version__,
    description='find yourself',
    long_description='',
    keywords='ha ha ha',
    author='Never Mind',
    author_email='',
    url='',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Testing'
    ],
    packages=find_packages(),
    include_package_data = True,
    install_requires=[
        'tornado',
        'requests',
        'sh',
        'derpconf==0.4.7',
    ],
)
