
n = int(raw_input())
n = int(n)

import math
def NumToStr(x):
    if x>15:
        return 1
    temp = x%5
    if temp ==5 or temp ==2:
        return 0
    else:
        return 1

for i in range(n):

    s =raw_input()
    s = int(s)
    a = NumToStr(s)
    if a==1:
        print "niu"
    else:
        print "yang"
