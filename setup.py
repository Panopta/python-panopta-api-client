from setuptools import setup, find_packages

setup(
    name='panopta_api',
    version='2.0.0',
    description='Panopta API Client',
    long_description=open('README.md').read(),
    license='MIT',
    author='Panopta',
    author_email='support@panopta.com',
    url='https://github.com/Panopta/python-panopta-api-client',
    packages=['panopta_api'],
    install_requires=['httplib2'],
)
