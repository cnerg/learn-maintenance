from setuptools import setup

setup(
    name = 'progPackage',
    entry_points={
        'console_scripts': [
            'prog = progPackage:prog.main',
        ],
    },
    install_requires = ['numpy',],
)