from setuptools import setup

setup(
    name="codeq",
    version='0.1',
    py_modules=['cli'],
    install_requires=[
        'Click', 'praw'
    ],
    entry_points='''
        [console_scripts]
        codeq=cli:main
    ''',
)
