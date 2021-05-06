#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-jennifer_plugin',
    version='0.0.1',
    author='jennifer hu',
    author_email='jiadajia@126.com',
    maintainer='jennifer hu',
    maintainer_email='jiadajia@126.com',
    license='MIT',
    url='https://github.com/jennifer hu/pytest-jennifer_plugin',
    description='this is a simple plugin for jennifer',
    long_description=read('README.rst'),
    py_modules=['pytest_jennifer_plugin'],
    python_requires='>=3.5',
    install_requires=['pytest>=3.5.0'],
    classifiers=[
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    entry_points={
        'pytest11': [
            'jennifer_plugin = pytest_jennifer_plugin',
        ],
    },
)
