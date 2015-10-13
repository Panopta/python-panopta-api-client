from setuptools import setup
import os

long_description = open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.md')).read()

setup(
    name='panopta_api',
    version='2.0.0',
    description='Panopta API Client',
    long_description=long_description,
    license='MIT',
    author='Panopta',
    author_email='support@panopta.com',
    url='https://github.com/Panopta/python-panopta-api-client',
    packages=['panopta_api'],
    install_requires=['requests', 'requests-toolbelt'],
)
