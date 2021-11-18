#!/usr/bin/env python

from operator import itemgetter
import sys

current_date = None
current_temperature = 0
date = None

# read the entire line from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # slpiting the data on the basis of tab we have provided in mapper.py
    date, temperature = line.split('\t', 1)
    # convert temperature (currently a string) to int
    try:
        temperature = int(temperature)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
    
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: temp) before it is passed to the reducer
    if current_date == date:
        if temperature > current_temperature:
            current_temperature = temperature
    else:
        if current_date:
            # write result to STDOUT
            print('%s\t%d' % (current_date, current_temperature))
        current_temperature = temperature
        current_date = date

# do not forget to output the last word if needed!
if current_date == date:
    print('%s\t%d' % (current_date, current_temperature))
