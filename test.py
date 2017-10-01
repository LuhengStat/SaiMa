s = raw_input()
s = s.split()
s = map(float, s)
m = s[0]
n = int(s[1])
temp = m
out = 0
for i in range(1, n+1):
    out = out + temp
    temp = temp ** (1 / 2.0)

print("%.2f" % out)

