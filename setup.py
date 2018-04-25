from setuptools import setup

setup(
    name="csv2sql",
    version='0.1',
    py_modules=['csv_to_sql'],
    install_requires=[
        'Click', 'pandas', 'numpy', 'sqlalchemy'
    ],
    entry_points='''
        [console_scripts]
        csv2sql=csv_to_sql:csv_2_sql
    ''',
)