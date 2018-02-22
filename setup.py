# -*- coding: utf-8 -*-
from setuptools import setup

import glob

setup(
    name='omegalines',
    version='0.1',
    author='Fabian Peter Hammerle',
    author_email='fabian@hammerle.me',
    url='https://github.com/fphammerle/omegalines',
    keywords=['public transportation', 'onion omega',
              'oled display', 'vienna', 'wiener linien',
              'öbb', 'oebb', 'departure monitor'],
    scripts=glob.glob('scripts/*'),
    install_requires=[
        'python-dateutil',
        'pyyaml',
    ],
    # tests_require=['pytest']
)
