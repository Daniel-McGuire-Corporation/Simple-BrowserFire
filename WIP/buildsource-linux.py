#!/usr/bin/env python3

import subprocess
import os

# Requirements
# - Memory: 4GB RAM minimum, 8GB+ recommended.
# - Disk Space: At least 50GB of free disk space.
# - Operating System: A 64-bit installation of Linux.

# Install Dependencies
subprocess.run(["sudo", "apt", "update"])
subprocess.run(["sudo", "apt", "install", "python3"])
subprocess.run(["sudo", "apt", "install", "python3-dev"])
subprocess.run(["sudo", "apt", "install", "mercurial"])

# Add Python user base bin directory to PATH
user_base_bin = os.path.expanduser("~/.local/bin")
with open(os.path.expanduser("~/.bashrc"), "a") as bashrc:
    bashrc.write(f'export PATH="{user_base_bin}:$PATH"\n')
subprocess.run(["source", "~/.bashrc"])

# Prompt user to set the clone path to ffox
print("Be sure to set the clone path to ffox")
input("Press Enter to continue...")
subprocess.run(["clear"])

# Setup devenv
subprocess.run(["curl", "-LO", "https://hg.mozilla.org/mozilla-central/raw-file/default/python/mozboot/bin/bootstrap.py"])
subprocess.run(["python3", "bootstrap.py"])

os.chdir("ffox")

# Add Simple Browser
subprocess.run(["curl", "-L", "-o", "SB.zip", "https://github.com/Daniel-McGuire-Corporation/SimpleBrowser-Fire/archive/refs/heads/main.zip"])
subprocess.run(["unzip", "SB.zip"])

# Build
subprocess.run(["./mach", "bootstrap"])
subprocess.run(["./mach", "build"])

print("Compiled! Run with ./mach run")