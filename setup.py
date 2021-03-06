from setuptools import setup, find_packages
from codecs import open
from os import path

if path.isfile('README.md'):
    try:
        import pypandoc
        long_description = pypandoc.convert('README.md', 'rst')
    except (IOError, ImportError):
        long_description = open('README.md').read()
else:
    long_description=""

setup(
    name='mobbage',

    description='A HTTP stress test and benchmark tool',
    long_description=long_description,
    url='https://github.com/redfin/mobbage',

    author='Eric Schwimmer',
    author_email='git@nerdvana.org',

    license='Apache 2.0',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: System Administrators',
        'Topic :: System :: Benchmark',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    keywords='http http/2 benchmark stress load test',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['requests', 'setuptools_scm'],
    setup_requires=['pytest-runner', 'setuptools_scm'],
    tests_require=['pytest'],
    use_scm_version=True,

    entry_points={
        'console_scripts': [
            'mobbage = mobbage:main'
        ],
    },
)
