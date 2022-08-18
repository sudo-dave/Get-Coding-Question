from setuptools import setup

setup(
    name="codeq",
    version='0.1',
    packages=["app"],
    install_requires=[
        'Click', 'praw'
    ],
    entry_points='''
        [console_scripts]
        codeq=app.cli:main
    ''',
)
