
nx = [3, 1]
ai = [1, 0, 1]

minai = min(ai)
pos = [i for i, x in enumerate(ai) if x == minai]
flag = 1
tmpnx = nx[1] -1


tmpnx = [-x + nx[1] - 1 for x in pos]
maxtmpnx = max(tmpnx)
tmppos = [i for i, x in enumerate(tmpnx) if x == maxtmpnx]
pos = [pos[tmppos[0]]]

if minai == 0:
    out = ai
else:
    out = [x-minai for x in ai]


if pos[0] > nx[1]-1:
    possecond = range(pos[0]+1, nx[0]) + range(0, nx[1])
else:
    possecond = range(pos[0]+1, nx[1])

out[pos[0]] = len(possecond) + minai*nx[0]
for i in possecond:
    out[i] = out[i] - 1

#out = [1,2,3]
tmpout =''
for i in range(0, len(out)-1):
    tmpout = tmpout + str(out[i]) + ' '
tmpout = tmpout + str(out[len(out)-1])

print tmpout

