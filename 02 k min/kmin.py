seqnum = int(raw_input())

wholeseq = []
for i in range(seqnum):
    tmps = raw_input()
    tmps = tmps.split()
    tmps = map(int, tmps)
    wholeseq = wholeseq +tmps
k = int(raw_input())

def arrayn(n):
    out = range(8)
    for i in range(8):
        out[i] = n ** i
    out = list(reversed(out))
    return out

wholeout = []
for j in range(1, int(k/seqnum)+3):
    tmparray = arrayn(j)
    for i in range(seqnum):
        temprange = range(i*8, (i+1)*8)
        tempseq = [wholeseq[l] for l in temprange]
        temp = sum([tempseq[l]*tmparray[l] for l in range(8)])
        wholeout.append(temp)

wholeout = sorted(wholeout)
finalout = wholeout[k-1]

print finalout


