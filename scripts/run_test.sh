#../dashing2/dashing2 sketch -k15 --topk 10 --parse-by-seq --edit-distance --compute-edit-distance ./covid19/toy.fasta --cmpout ./knnGraph_covid.txt -F table_covid.txt

#../dashing2/dashing2 sketch -k15 --parse-by-seq --square ./covid19/toy.fasta --cmpout  table_covid.txt
#../dashing2/dashing2 sketch -k15 --parse-by-seq --square --edit-distance --compute-edit-distance ./covid19/toy.fasta --cmpout  table_covid_OMH.txt
../dashing2/dashing2 sketch -k25 --parse-by-seq --square ./ecoli/ecoli_merge.fasta --cmpout  table_ecoli.txt
../dashing2/dashing2 sketch -k25 --parse-by-seq --square --edit-distance --compute-edit-distance ./ecoli/ecoli_2.fasta --cmpout  table_ecoli_OMH.txt
#../dashing2/dashing2 sketch -k50 --topk 10 --parse-by-seq --edit-distance --compute-edit-distance ./ecoli/ecoli.fasta --cmpout ./knnGraph_ecoli.txt
