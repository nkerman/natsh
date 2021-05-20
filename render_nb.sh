#!/bin/zsh

# Specify a list of paths
# case help/code from:
##https://stackoverflow.com/questions/7069682/how-to-get-arguments-with-flags-in-bash


Process='RENDER'
if [ $# -gt 0 ]; then
    echo "Make sure if you specify outdir that -o then directory path come first!"
    echo "Running $Process on file(s)"

    mkdir -p ~/Desktop/.temp.nosync
    mkdir -p ~/Desktop/.temp.nosync/clear
    mkdir -p ~/Desktop/.temp.nosync/render
fi

while test $# -gt 0; do
  case "$1" in
    -h|--help)
      echo "$package - attempt to capture frames"
      echo " "
      echo "$package [options] application [arguments]"
      echo " "
      echo "options:"
      echo "-h, --help                show brief help"
      echo "-o, --output-dir=DIR      specify a directory to store output in. -o then path to dir must come first!"
      exit 0
      ;;

    -o|--output-dir)
      shift
      if test $# -gt 0; then
        export OUTDIR=$1
        echo "Will save to output directory = $OUTDIR"
      else
        echo "no output directory specified"
        exit 1
      fi
      shift
      ;;
    *)
      echo $OUTDIR
      echo "Filepath: $1"
      cp $1 ~/Desktop/.temp.nosync/clear
      jupyter-nbconvert --to html $1 --output-dir=$OUTDIR --ExecutePreprocessor.timeout=1500
      shift 
      ;;
  esac
done