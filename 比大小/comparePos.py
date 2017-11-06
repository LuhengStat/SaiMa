n = int(raw_input())
largest = []
nownum = 0

import math
for i in range(n):
    words = raw_input()
    wlen = len(words)
    out = 1
    for j in range(wlen):
        temp = 0
        for m in words[j:]:
            if words[j] > m:
                temp = temp + 1
        out = out + math.factorial(11-j)*temp
    print out

