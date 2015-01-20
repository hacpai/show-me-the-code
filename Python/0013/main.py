import re

pattern = '[a-z]'
stopword = ""

for line in iter( raw_input, stopword ):
    sum = 0
    line = line.lower()
    for i in line:
        is_pattern = re.search ( pattern, i )
        if is_pattern:
            sum += ord(i) - ord('a') + 1
        else:
            sum += 0
    print sum
