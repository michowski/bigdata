./mapper.py < input/datasource1/part-00000 | sort -t $'\t' -k1,1 | ./reducer.py
