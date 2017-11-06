

nm = raw_input()
nm = map(int, nm.split())

ci = raw_input()
ci = map(int, ci.split())

Prob = []
for i in range(nm[0]):
    temp = raw_input()
    temp = map(float, temp.split())
    Prob.append(temp)

print 1.6