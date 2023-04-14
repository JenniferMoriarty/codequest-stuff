import sys
import math
import string

#get the first number (the number of lines to read)
cases = int(sys.stdin.readline().rstrip())

#use the variable on line 6 to read that many lines
for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    # Iterate over index
    for element in range(0, len(line)):
        if line[element] == 'a' or line[element] == 'e' or line[element] == 'i' or line[element] == 'o' or line[element] == 'u':
            if line[element-2] == 'a' or line[element-2] == 'e' or line[element-2] == 'i' or line[element-2] == 'o' or line[element-2] == 'u':
                print(line[element+1], end = "")
            elif line[element-1] != 'a' and line[element-1] != 'e' and line[element-1] != 'i' and line[element-1] != 'o' and line[element-1] != 'u':
                print(line[element+1], end = "")
    print()
    
    


