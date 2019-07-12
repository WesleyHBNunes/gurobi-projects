#!/bin/bash
files[0]=shirts_4
files[1]=shirts_8
files[2]=shirts_12
files[3]=shirts_16
 
for i in {0..3}
do
    python3 Tests.py ${files[i]} > Results/${files[i]}.txt
done