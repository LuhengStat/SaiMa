nl = raw_input()
pos = raw_input()
nl = map(int, nl.split())
pos = map(int, pos.split())

def distance(nl, pos):
    pos = sorted(pos)
    diff = [pos[i + 1] - pos[i] for i in range(len(pos) - 1)]
    maxlen = max(diff)
    if pos[0] == 0 and pos[len(pos)-1] == nl[1]:
        return maxlen/2.0
    else:
        return max(maxlen / 2.0, pos[0] - 0, nl[1] - pos[len(pos)-1])

out = distance(nl, pos)

print "%.2f" % out


