#!/bin/zsh

# Specify a list of paths

Process='CLEAR'
if [ $# -gt 0 ]; then
    echo "Running $Process on $# file(s)"

    mkdir -p ~/Desktop/.temp.nosync
    mkdir -p ~/Desktop/.temp.nosync/clear
    mkdir -p ~/Desktop/.temp.nosync/render


    while [ "$1" != "" ]; do
        echo "Filepath: $1"
        cp $1 ~/Desktop/.temp.nosync/clear
        jupyter-nbconvert --ClearOutputPreprocessor.enabled=True --inplace $1

        # Shift all the parameters down by one
        shift
    done

else
    echo "No files specified"
fi
