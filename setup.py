from setuptools import setup

setup(
    entry_points = {
        'console_scripts': ['prog = src.prog_package.prog:main',],
    }
)