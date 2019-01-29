#!/bin/bash

FILE="/rsgrps/bh_class/sbrown10/biosys-analytics/assignments/02-bash-scripting/$1"

if [[ $# -eq 0 ]]; then
    echo "Usage: cat-n.sh FILE"
    exit 1
fi


if [[ ! -f "$1" ]]; then
    echo "$1 is NOT a file"
    exit 1
fi


k=0
while read -r LINE; do
    k=$((k+1))
    echo $k "$LINE"
done < "$FILE"
