#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()


setup(
    name='python-todotxt',
    version='0.1.2',
    description="Simple python library for todo.txt file format",
    long_description=readme,
    author="Bogdan Gladyshev",
    author_email='siredvin.dark@gmail.com',
    url='https://gitlab.com/SirEdvin/python-todotxt',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
    ],
    license="MIT license",
    zip_safe=False,
    keywords='todo.txt',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
    tests_require=[],
    setup_requires=[],
)
