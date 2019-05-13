#!/bin/bash

CURDIR=$(pwd)
BASEDIR=$(dirname $0)

cd $BASEDIR/..
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps smashggpy
cd $CURDIR