#!/usr/bin/env python
  
# import sys because we need to read and write data to STDIN and STDOUT
import sys

# reading entire line from STDIN (standard input)
for line in sys.stdin:
    # to remove leading and trailing whitespace
    line = line.strip()
    date = line[15:23]
    quality = int(line[92])
    temperature = int(line[87:92])
    # Invalid records have flag other than 01459
    if ((quality == 0) or (quality == 1) or (quality == 4) or (quality == 5) or (quality == 9)):
        if ((temperature != 9999)):
            print('%s\t%d' % (date, int(line[87:92])))
