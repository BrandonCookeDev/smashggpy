#!/bin/bash

CURDIR=$(pwd)
BASEDIR=$(dirname $0)

cd $BASEDIR/..
python3 -m pip install --user --upgrade setuptools wheel
python3 setup.py sdist bdist_wheel
cd $CURDIR