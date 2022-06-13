#!/usr/bin/env python
import os
from setuptools import setup, find_packages

__version__ = "0.0.3"


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="rytr",
    version=__version__,
    author="MarcosAguayo",
    author_email="marcos@aguayo.es",
    url="https://marcosaguayo.com/",
    description="Python package for RYTR",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    download_url="https://github.com/maguayo/rytr-python",
    packages=find_packages(),
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[],
    license="GPL-3",
    extras_require={},
)
