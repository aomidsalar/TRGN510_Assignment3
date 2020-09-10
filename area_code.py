#!usr/bin/python
import fileinput
import sys
import re

phone_numbers= sys.argv[1]
for each_line_of_text in fileinput.input(phone_numbers):
    numbers = re.sub(r'\D','', each_line_of_text)
    AreaCodes=numbers[0:3]
    print (AreaCodes)


