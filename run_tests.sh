#!/bin/bash

if [ -d $HOME/anaconda3 ]
then
    export PATH="$HOME/anaconda3/bin:$PATH"
elif [ -d $HOME/miniconda ]
then
    export PATH="$HOME/miniconda/bin:$PATH"
fi

if [[ "$TRAVIS_PYTHON_VERSION" == "2.7" ]]
then
    PYTHON=python2
else
    PYTHON=python3
fi

for path in $(ls -d session*)
do
    if [ -d $path/test ]
    then
        name=$(basename $path)
        echo "Testing $name"
        ( cd $path ; if [ -d requirements.txt ] ; then source activate $name ; fi ; $PYTHON -mpytest )
    fi
done