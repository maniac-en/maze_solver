from setuptools import setup

setup(
    name='maniac_maze_solver',
    version='0.1',
    py_modules=['main'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        mms=main:main
    ''',
)
