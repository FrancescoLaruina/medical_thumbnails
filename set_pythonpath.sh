#!/bin/bash
# Reference: http://stackoverflow.com/questions/59895/getting-the-source-directory-of-a-bash-script-from-within
SETUP_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
echo "medical_thumbnails root is in $SETUP_DIR"
export PYTHONPATH=$SETUP_DIR:$PYTHONPATH
echo "PYTHONPATH set to $PYTHONPATH"
