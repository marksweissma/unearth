train(){
    for i in $(ls $1); do
    awk  -F"," 'FNR > 1 {print $1","$14","$15","$16","$18","$20","$21","$25}' $i > 'temp.csv'
    cat 'temp.csv' >> $2
    done
    rm 'temp.csv'
    }
