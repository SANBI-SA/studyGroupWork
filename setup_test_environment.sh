#!/bin/bash

for path in $(ls -d session*)
do 
    name=$(basename $path)
    if [ -e $path/requirements.txt ]
    then 
        conda create -y -n $name --file $path/requirements.txt
    fi 
done
  