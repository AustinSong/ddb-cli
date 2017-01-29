from setuptools import setup

setup(
    name='pyddb',
    version='0.1',
    py_modules=['pyddb'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        pyddb=pyddb:main
    ''',
)
