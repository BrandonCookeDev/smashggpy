#!/bin/bash

CURDIR=$(pwd)
BASEDIR=$(dirname $0)

cd $BASEDIR/..
rm -Rf dist
rm -Rf *.egg-info
cd $CURDIR

$BASEDIR/pack.sh && $BASEDIR/upload.sh