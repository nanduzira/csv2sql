from setuptools import setup

setup(
    name="csv2sql",
    version='0.1',
    py_modules=['hello'],
    install_requires=[
        'Click', 'pandas', ''
    ],
    entry_points='''
        [console_scripts]
        csv2sql=hello:cli
    ''',
)