#!/usr/bin/env python
from __future__ import unicode_literals
from setuptools import setup, find_packages

install_requires = [
    "Jinja2==2.8",
    "boto==2.13.3",
    "flask==0.10.1",
    "httpretty==0.8.10",
    "requests==2.9.1",
    "xmltodict==0.9.0",
    "six>=1.10.0",
    "Werkzeug==0.10.4",
]

extras_require = {
    # No builtin OrderedDict before 2.7
    ':python_version=="2.6"': ['ordereddict==1.1'],
}

setup(
    name='moto',
    version='0.4.24.3',
    description='A library that allows your python tests to easily'
                ' mock out the boto library',
    author='Steve Pulec',
    author_email='spulec@gmail.com',
    url='https://github.com/spulec/moto',
    entry_points={
        'console_scripts': [
            'moto_server = moto.server:main',
        ],
    },
    packages=find_packages(exclude=("tests", "tests.*")),
    install_requires=install_requires,
    extras_require=extras_require,
    license="Apache",
    test_suite="tests",
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Software Development :: Testing",
    ],
)
