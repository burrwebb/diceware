from setuptools import setup
import diceware.__version__ as version_string

setup(
    name='ideal_waffle',
    version=version_string,
    description='A module for creation of diceware passphrases',
    license='MIT',
    packages=['ideal_waffle'],
    author='Burr Webb',
    author_email='burrwebb@gmail.com',
    keywords=['example'],
    url='https://www.risksense.com',
    install_requires=[
        'requests',
    ]
)