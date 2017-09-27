
import math
def NumToStr(x):
    flag = 1
    num = x/26
    out = 'Z'*num
    diff = x - num*26
    starts = 'A'
    if diff > 0:
        tmpstr = chr(ord(starts) + diff)
        out = out + tmpstr
    return out

def NumToStr(x):
    flag = 1
    out = []
    while flag:
        if x == 0:
            a = 0
            flag = 0
        else:
            a = int(math.log(x) / math.log(26))
            x = x - 26 ** a
            out.append(a)
    return out

def StrToNum(str):
    out = 0
    for i in range(len(str)):
        out = out + ord(str[i]) - ord('A') + 1
    return out

def judgeRxCy(str):
    def startpos(str):
        for i in range(len(str)):
            temp = str[i].isalpha()
            if temp == 0:
                return i

    pos = startpos(str)
    out = [str[i].isalpha() for i in range(len(str))]

    if sum([out[i] for i in range(pos, len(str))]) > 0:
        return 1
    else:
        return 0

def RxCyToAlNum(str):
    ColPos = 0
    for i in range(len(str)):
        if str[i] == 'C':
            ColPos = i
    Colnum = [str[i] for i in range(ColPos+1, len(str))]
    Rownum = [str[i] for i in range(1, ColPos)]
    Colnum = int("".join(Colnum))
    Rownum = "".join(Rownum)
    out = NumToStr(Colnum) + Rownum
    return out

def AllNumToRxCy(str):
    ColPos = 0
    for i in range(len(str)):
        if not str[i].isalpha():
            ColPos = i
            break
    Rownum = [str[i] for i in range(0, ColPos)]
    Rownum = "".join(Rownum)
    Rownum = StrToNum(Rownum)
    Colnum = [str[i] for i in range(ColPos, len(str))]

