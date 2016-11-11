# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name="crypto",
    description="Cryptography challenges",
    version='0.0.1',
    author="Zach Rickert",
    author_email="zachrickert@gmail.com",
    license='MIT',
    py_modules=['set1'],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={'test': ['pytest', 'tox']},
)
