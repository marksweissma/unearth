#!/usr/bin/sh
# sh clean.sh <directory> <name*> <output>
for i in $(find $1 -name $2); do
awk  -F"," 'FNR > 1 {print $1","$14","$15","$16","$18","$20","$21","$25}' $i > 'temp.csv'
cat 'temp.csv' >> $3
done
rm 'temp.csv'
