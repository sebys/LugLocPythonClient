#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'requests'
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='luglocapiclient',
    version='0.1.2',
    description="Simpleapi client for LugLoc",
    long_description=readme + '\n\n' + history,
    author="Sebis Henzenn",
    author_email='sebys@hotmail.com',
    url='https://github.com/sebys/luglocapiclient',
    packages=[
        'luglocapiclient',
    ],
    package_dir={'luglocapiclient':
                 'luglocapiclient'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='luglocapiclient',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
