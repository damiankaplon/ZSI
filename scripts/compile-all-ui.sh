#!/bin/bash
for i in ./QtDesigner/*.ui; do
    pyuic5 -x "$i" -o "$i.py"
done