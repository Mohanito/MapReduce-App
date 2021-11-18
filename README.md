# MapReduce-App
A Hadoop MapReduce application to find the maximum temperature in every day of the years 1901 and 1902 from the NCDC weather records. Deployed on Google Cloud Platform.

## Test mapper and reducer on local machine
    cat data/1902 | python mapper.py | sort -k1,1 | python reducer.py

## Run the MapReduce job on the cluster
    hadoop jar /usr/lib/hadoop/hadoop-streaming.jar \
    -files mapper.py,reducer.py \
    -input /data/* \
    -output /output \
    -mapper mapper.py \
    -reducer reducer.py
    -combiner reducer.py \

## Manually clean up CRLF to LF
https://stackoverflow.com/questions/43048654/hadoop-python-subprocess-failed-with-code-127
    sed -i -e 's/\r$//' mapper.py
    sed -i -e 's/\r$//' reducer.py