#!/bin/sh

INSTALL_DIR="/usr/local/bin"

if [ ! -f /usr/bin/python3 ]; then
	echo "Error! Python 3 not found, but is required!"
	exit 1
fi

echo "This program will install the makeNewFile program into $INSTALL_DIR, using magical sudo powers."



sudo cp makeNewFile.py $INSTALL_DIR/makeNewFile
