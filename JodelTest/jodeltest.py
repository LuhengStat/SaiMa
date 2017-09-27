s = raw_input()
star = raw_input()

def jodelcode(s, star):
    score = 0
    out = []
    for i in range(len(s)):
        if s[i].isalnum():
            out.append("1")
            if star[i] == "1":
                score = score + 1
        else:
            out.append("0")
            if star[i] == "0":
                score = score + 1
    return score/(len(s)+0.0)

out = jodelcode(s, star)*100
print "%.2f%%" % out

