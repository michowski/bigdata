 rm -rf output && mapred streaming \
-files mapper.py,reducer.py \
-input input/station.csv -output output \
-mapper mapper.py -reducer reducer.py
