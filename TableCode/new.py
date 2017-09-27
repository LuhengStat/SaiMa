
n = int(raw_input())
largest = []
nownum = 0

for i in range(n):

    s =raw_input()
    import math

    def NumToStr(num):
        letters = ''
        while num:
            mod = (num - 1) % 26
            letters += chr(mod + 65)
            num = (num - 1) // 26
        return ''.join(reversed(letters))


    def StrToNum(col_str):
        expn = 0
        col_num = 0
        for char in reversed(col_str):
            col_num += (ord(char) - ord('A') + 1) * (26 ** expn)
            expn += 1
        return col_num


    def judgeRxCy(string):
        def startpos(string):
            for i in range(len(string)):
                temp = string[i].isalpha()
                if temp == 0:
                    return i

        pos = startpos(string)
        out = [string[i].isalpha() for i in range(len(string))]

        if sum([out[i] for i in range(pos, len(string))]) > 0:
            return 1
        else:
            return 0


    def RxCyToAlNum(string):
        ColPos = 0
        for i in range(len(string)):
            if string[i] == 'C':
                ColPos = i
        Colnum = [string[i] for i in range(ColPos + 1, len(string))]
        Rownum = [string[i] for i in range(1, ColPos)]
        Colnum = int("".join(Colnum))
        Rownum = "".join(Rownum)
        out = NumToStr(Colnum) + Rownum
        return out


    def AllNumToRxCy(string):
        ColPos = 0
        for i in range(len(string)):
            if not string[i].isalpha():
                ColPos = i
                break
        Colnum = [string[i] for i in range(0, ColPos)]
        Colnum = "".join(Colnum)
        Colnum = StrToNum(Colnum)
        Colnum = str(Colnum)
        Rownum = [string[i] for i in range(ColPos, len(string))]
        Rownum = "".join(Rownum)
        out = "R" + Rownum + "C" + Colnum
        return out


    if judgeRxCy(s):
        print RxCyToAlNum(s)
    else:
        print AllNumToRxCy(s)
