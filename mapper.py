#!/usr/bin/env python
  
# import sys because we need to read and write data to STDIN and STDOUT
import sys

# reading entire line from STDIN (standard input)
for line in sys.stdin:
    # to remove leading and trailing whitespace
    line = line.strip()
    temperature = int(line[87:92])
    if ((temperature != 9999)):
        print('%s\t%d' % (line[15:19], int(line[87:92])))
