# MapReduce-App
A Hadoop MapReduce application to find the maximum temperature in every day of the years 1901 and 1902 from the NCDC weather records. Deployed on Google Cloud Platform.

## Test mapper and reducer on local machine
    cat data/1902 | python mapper.py | sort -k1,1 | python reducer.py
