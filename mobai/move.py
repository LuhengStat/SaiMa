

n = 4
num = [1, 2, 3, 4]

sortnum = sorted(num)
minnum = min(num)
pos = [i for i, x in enumerate(num) if x == minnum]
pos = pos[0]

def Compare(sortnum, num, pos):
    for tmppos in range(len(num)):
        if pos == len(num) - 1:
            return pos
        if sortnum[tmppos] == num[pos]:
            pos = pos + 1
            out = tmppos
        else:
            return out
    return out
out = Compare(sortnum, num, pos)

res = n - out - 1

print res
