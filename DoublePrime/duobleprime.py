s = raw_input()
s = int(s)

def isprime(x):
    num = int(x/2)+1
    out = 1
    for i in range(2, num+1):
        if x % i == 0:
            return 0
    return out

def doubleprime(x):
    tempx = str(x)
    revtempx = [tempx[i] for i in reversed(range(len(tempx)))]
    revtempx = "".join(revtempx)
    revx = int(revtempx)
    if x != revx and isprime(x) and isprime(revx):
        return 1
    else:
        return 0

flag = 0
num = 12
while flag < s and num <= 10**6:
    if doubleprime(num):
        out = num
        flag = flag + 1
    num = num + 1

finalout = out
print finalout

out =[]
for i in range(1, 10**4):
    if isprime(i):
        out.append(i)

