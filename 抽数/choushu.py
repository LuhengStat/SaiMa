s = raw_input()
s = map(int, s.split())

flag = 0
change = []
while flag < s[1]:
    tmp = raw_input()
    change.append(int(tmp))
    flag = flag + 1

n = s[0]
out = range(1, n+1)
for i in range(len(change)):
    temp = change[i]
    pos = [i for i, x in enumerate(out) if x == temp]
    tempout = []
    for j in range(n):
        if j != pos[0]:
            tempout.append(out[j])
    out = [temp] + tempout

for i in range(n):
    print out[i]