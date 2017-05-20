#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'attrs~=17.0',
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='pyrules',
    version='0.1.0',
    description="A Python rules engine inspired by OPS5.",
    long_description=readme + '\n\n' + history,
    author="Christopher Petrilli",
    author_email='petrilli@amber.org',
    url='https://github.com/petrilli/pyrules',
    packages=[
        'pyrules',
    ],
    package_dir={
        'pyrules': 'pyrules'
    },
    include_package_data=True,
    install_requires=requirements,
    license="BSD license",
    zip_safe=False,
    keywords='pyrules',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
