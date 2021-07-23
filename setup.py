"""
The type hinting flake8 plugin.
"""
import setuptools

requires = [
    "flake8 > 3.0.0",
    "importlib_metadata"
]

flake8_entry_point = "flake8.extension"

setuptools.setup(
    name="flake8-typehinting",
    license="MIT",
    version="0.1.0",
    description="Type Hinting Flake8 Extension",
    author="Gage Larsen",
    author_email="gagelarsen53@gmail.com",
    url="https://github.com/gagelarsen/flake8-typehinting",
    packages=[
        'flake8_typehinting',
    ],
    install_requires=requires,
    entry_points={
        flake8_entry_point: [
            'TH = flake8_typehinting:Plugin',
        ],
    },
    classifiers=[
        "Framework :: Flake8",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
)
