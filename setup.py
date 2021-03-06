#!/usr/bin/env python
# Copyright (C) 2015-2016 Jurriaan Bremer.
# This file is part of SFlock - http://www.sflock.org/.
# See the file 'docs/LICENSE.txt' for copying permission.

from setuptools import setup

setup(
    name="SFlock",
    version="0.2.2",
    author="Jurriaan Bremer",
    author_email="jbr@cuckoo.sh",
    packages=[
        "sflock",
        "sflock.unpack",
        "sflock.data",
    ],
    entry_points={
        "console_scripts": [
            "sflock = sflock.main:main",
        ],
    },
    url="http://sflock.org/",
    license="GPLv3",
    description="Sample staging and detonation utility",
    include_package_data=True,
    install_requires=[
        "click==6.6",
        "olefile==0.43",
        "python-magic==0.4.12",
    ],
)
