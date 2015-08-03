import os
from setuptools import setup, find_packages

def readfile(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='preprocessor',
    version='1.0.9',
    description='Preprocessor for files.',
    long_description=readfile('README.md'),
    ext_modules=[],
    packages=find_packages(),
    py_modules = [],
    scripts=['scripts/preprocessor'],
    author='Szymon Sidor',
    author_email='szymon.sidor@gmail.com',
    url='https://github.com/nivwusquorum/preprocessor',
    download_url='https://github.com/nivwusquorum/preprocessor',
    keywords='Macros,Processing,FileIO',
    license='MIT',
    platforms='any',
    zip_safe=False,
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.3',
    ],
    setup_requires = [],
    include_package_data=True,
)
