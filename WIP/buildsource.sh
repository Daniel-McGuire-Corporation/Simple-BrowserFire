#!/bin/bash

# Requirements:
# - Memory: 4GB RAM minimum, 8GB+ recommended.
# - Disk Space: At least 50GB of free disk space.
# - Operating System: A 64-bit installation of Linux.

# Install Dependencies
sudo apt update
sudo apt install python3 python3-dev
sudo apt install mercurial

# Add Python user base bin directory to PATH
echo 'export PATH="$(python3 -m site --user-base)/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

# Prompt user to set the clone path to ffox (Firefox source code repository)
echo "Be sure to set the clone path to ffox"
read -n1 -r -p "Press any key to continue..."
clear

# Setup devenv
curl -LO https://hg.mozilla.org/mozilla-central/raw-file/default/python/mozboot/bin/bootstrap.py
python3 bootstrap.py


cd ffox

# Add Simple Browser
curl -L -o SB.zip https://github.com/Daniel-McGuire-Corporation/SimpleBrowser-Fire/archive/refs/heads/main.zip
unzip SB.zip

# Compile
./mach bootstrap
./mach build

echo "Compiled! Run with ./mach run
