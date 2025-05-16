#!/bin/bash

# Set origin (your fork)
git remote set-url origin https://github.com/tazmanian60/openhouseparty.online.git

# Add upstream (production source)
git remote add upstream https://github.com/Perfectfire33/openhouseparty.online.git

# Fetch upstream changes
git fetch upstream

# Merge upstream/main into your current branch
git merge upstream/main

# Create and switch to new dev snapshot branch
DATE=$(date +%Y_%m_%d)
git checkout -b v$DATE

echo "✔ Git remotes set and v$DATE branch created."
