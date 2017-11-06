
n = int(raw_input())
n = int(n)

import math
def NumToStr(x):
    flag = 1
    out = []
    while flag:
        if x == 0:
            a = 0
            flag = 0
        else:
            a = int(math.log(x) / math.log(4))
            x = x - 4 ** a
            out.append(a)
    return out

for i in range(n):

    s =raw_input()
    s = int(s)
    a = NumToStr(s)
    if len(a)%2==1:
        print "niu"
    else:
        print "yang"
