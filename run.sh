 rm -rf output && mapred streaming \
-files mapper.py,reducer.py \
-input input/datasource1 -output output \
-mapper mapper.py -reducer reducer.py -combiner reducer.py
