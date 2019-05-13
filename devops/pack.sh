#!/bin/bash

CURDIR=$(pwd)
BASEDIR=$(dirname $0)

cd $BASEDIR/..
python3 setup.py sdist
cd $CURDIR