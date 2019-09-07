""" ===================================================================================================================
|
|   Name      :  setup.py
|   Module    :  ideal_waffle
|   Copyright :  2019 Burr Webb
|   License   :  MIT  (https://choosealicense.com/licenses/mit)
|
=================================================================================================================== """

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
    keywords=['diceware'],
    url='https://github.com/burrwebb/ideal-waffle',
    install_requires=[
        'requests'
    ]
)


"""
    Copyright 2019 Burr Webb
    
    Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
    associated documentation files (the "Software"), to deal in the Software without restriction,
    including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
    and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
    subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in all copies or
    substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
    LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
    IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
    WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
    SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
