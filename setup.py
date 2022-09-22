#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: atekawade
"""

from setuptools import setup, find_packages

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='tomo2mesh',
    url='https://github.com/aniketkt/Tomo2Mesh',
    author='Aniket Tekawade, Yashas Satapathy, Viktor Nikitin',
    author_email='atekawade@anl.gov',
    # Needed to actually package something
    packages=find_packages(),
    # Needed for dependencies
    install_requires=['numpy', 'pandas', 'scipy', 'h5py', 'matplotlib', 'scikit-image',\
                      'tqdm', 'ipython', 'seaborn',\
                      'pandas', 'tifffile'],
    version=open('VERSION').read().strip(),
    license='BSD',
    description='Toolkit for reconstructing tomography data as a polygonal mesh',
#     long_description=open('README.md').read(),
)


