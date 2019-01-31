#!/bin/bash

FILE="$1"

if [[ $# -eq 0 ]]; then
    echo "Usage: cat-n.sh FILE"
    exit 1
fi


if [[ ! -f "$1" ]]; then
    echo "$1 is not a file"
    exit 1
fi


k=0
while read -r LINE; do
    k=$((k+1))
    echo $k "$LINE"
done < "$FILE"
