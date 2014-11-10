#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except:
    from distutils.core import setup, find_packages

setup(
    name='dap2rpm',
    version='0.0.1',
    description='Generate RPM specfile for DevAssistant DAP packages',
    long_description=''.join(open('README.rst').readlines()),
    keywords='DevAssistant, DAP, RPM, specfile',
    author='Bohuslav Kabrda',
    author_email='bkabrda@redhat.com',
    license='GPLv2',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        ]
)
