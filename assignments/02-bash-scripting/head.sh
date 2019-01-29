#!/bin/bash

FILE="/rsgrps/bh_class/sbrown10/biosys-analytics/assignments/02-bash-scripting/$1"
lines=${2:-3}

if [[ $# -eq 0 ]]; then
    echo "Usage: head.sh FILE"
    exit 1
fi


if [[ ! -f "$1" ]]; then
    echo "$1 is not a file"
    exit 1
fi


i=0
while read -r lines; do
    echo "$lines"
    i=$((i+1))
    if [[ $i -eq $2 ]]; then
        break
    fi
done < "$FILE"
