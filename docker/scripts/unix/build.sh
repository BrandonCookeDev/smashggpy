#!/bin/bash

CURDIR=$(pwd)
BASEDIR=$(dirname $0)
IMAGE_NAME=$(cat $BASEDIR/../ImageName.txt)

echo Building Docker Image: $IMAGE_NAME

cd $BASEDIR/../../..
docker build -t $IMAGE_NAME .
cd $CURDIR