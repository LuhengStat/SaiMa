
n = int(raw_input())
n = int(n)

s = raw_input()
s = map(int, s.split())

def judge(s, i, j):
    if abs(i-j)==1:
        return 1
    if s[i] == s[j]:
        return 0
    subs = [s[t] for t in range(i+1, j)]
    temp = min(s[i], s[j])
    if max(subs) <= temp:
        return 1
    else:
        return 0

xor = []
success = []
for i in range(n):
    for j in range(i+1, n):
        tempjudge = judge(s, i, j)
        if tempjudge==1:
            temp = s[i] ^ s[j]
            xor.append(temp)

out = max(xor)
print out






