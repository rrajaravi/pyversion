from setuptools import setup
import os

def read_me():
    return open(os.path.join(os.path.dirname(__file__), 'README.rst'), 'r').read()

setup(
    name='pyversion',
    packages=['pyversion'],
    version='1.0',
    description='version checker for python library',
    long_description=read_me(),
    author='rajaravi',
    author_email='r.rajaravi@gmail.com',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Intended Audience :: Developers'
    ],
    test_suite='tests',
    install_requires=[],
    include_package_data=True,
    license='MIT License'
)
