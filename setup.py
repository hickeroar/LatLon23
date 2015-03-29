from setuptools import setup

setup(
    name = 'LatLon23',
    packages = [
        'LatLon23'
    ],
    version = '1.0.7',
    description = 'Methods for representing geographic coordinates',
    long_description = open('README.rst', 'r').read(),
    author  = 'Gen Del Raye, Ryan Vennell',
    author_email = 'gdelraye@hawaii.edu, ryan.vennell@gmail.com',
    maintainer = 'Ryan Vennell',
    maintainer_email = 'ryan.vennell@gmail.com',
    url = 'https://github.com/hickeroar/LatLon23',
    keywords = ['latitude', 'longitude', 'decimal degrees', 'degree minutes', 'distance'],
    install_requires = [
        'pyproj'
    ],
    classifiers = [
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering",
        "Development Status :: 4 - Beta",
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ]
)