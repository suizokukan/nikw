#!/usr/bin/env bash

VERSION="tests.sh v.1/2022-04-26"

# ---- --help ----------------------------------------------------------------
if [[ $1 = "--help" ]] || [[ $1 = "-h" ]]; then
    echo "$VERSION"
    echo "tests.sh : launch all the tests in tests/ ."
    echo "This script is a wrap around '$ python3.9 -m unittest tests/*.py'"
    echo ""
    echo "No argument required but you may use:"
    echo "-h / --help   : see this message."
    echo "-v / --version: see version string."
    exit 255
elif [[ $1 = "--version" ]] || [[ $1 = "-v" ]]; then
    echo "$VERSION"
    exit 255
fi

# ==== REAL WORK =============================================================
poetry run python3.10 -m unittest tests/*.py

exit 0
