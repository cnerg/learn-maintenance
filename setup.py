from setuptools import setup
setup(
    entry_points = {
        'console_scripts': ['prog = test_package.prog.cmd:main']
    }
)