# -*-coding:utf-8-*-
# !/usr/bin/env python

from setuptools import setup, find_packages

REQUIREMENTS = [
    'javalang>=0.11.0'
]

PKGS = find_packages(exclude=['tests'])
# PKG_DATA = [
#     ("bower_components", ['*']),
#     ("gui", ['*']),
#     ("output", ['*']),
#     (".", ['index.html', 'bower.json'])
# ]

VERSION = 0.1

setup(
    name='AnalysisProjectDependencies',
    version=VERSION,
    license='BSD',
    url='https://github.com/Kyson/AnalysisProjectDependencies',
    author='Kyson',
    author_email='kysonchao@gmail.com',
    description='Analysis project dependence(support java project)',
    packages=PKGS,
    package_files={},
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: BSD License',
    ],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=REQUIREMENTS,
    extras_require={
    }
)
