from importlib_metadata import entry_points

entry_points = {
    'console_scripts': ['prog = test_package.prog.cmd:main']
}