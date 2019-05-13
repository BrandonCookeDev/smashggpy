#!/bin/bash

CURDIR=$(pwd)
BASEDIR=$(dirname $0)

cd $BASEDIR/..
python3 -m pip install --user --upgrade twine
python3 -m twine upload dist/*
cd $CURDIR