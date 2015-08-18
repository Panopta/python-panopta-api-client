from setuptools import setup, find_packages

setup(
    name='panopta_rest_api',
    version='1.1.0',
    description='Panopta REST API Client',
    long_description=open('README.md').read(),
    license='MIT',
    author='Panopta',
    author_email='support@panopta.com',
    url='https://github.com/Panopta/python-panopta-api-client',
    py_modules=['api_client'],
    install_requires=['httplib2'],
)
