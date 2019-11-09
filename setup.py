import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "bound to leap",
    version = "0.0.1",
    author = "Nigel Haney",
    author_email = "",
    description = ("My entry into the Github Game Off 2019 competition."),
    license = "Apache",
    url = "",
    packages=['boundtoleap'],
    long_description=read('README.md'),
)