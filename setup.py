from setuptools import setup

setup(
    name                = 'LatLon23',
    packages            = ['LatLon23'],
    version             = '1.0.3',
    description         = 'Methods for representing geographic coordinates',
    author              = 'Gen Del Raye, Ryan Vennell',
    author_email        = 'gdelraye@hawaii.edu, ryan.vennell@gmail.com',
    maintainer          = 'Ryan Vennell',
    maintainer_email    = 'ryan.vennell@gmail.com',
    url                 = '',
    download_url        = '',
    keywords            = ['latitude', 'longitude', 'decimal degrees', 'degree minutes', 'distance'],
    install_requires    = ['pyproj'],
    package_data        = {},
    classifiers         = [
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering",
        "Development Status :: 4 - Beta"
    ]
)