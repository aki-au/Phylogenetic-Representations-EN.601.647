/usr/bin/time --format='user= %U system= %S elapsed= %e CPU= %P MemMax= %M'  ../dashing2/dashing2 sketch -k15 --parse-by-seq --square --edit-distance --compute-edit-distance $1 --cmpout  $2
