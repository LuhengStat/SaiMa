n = int(raw_input())
largest = []
nownum = 0

for i in range(n):
    Change = raw_input()
    Change = map(int, Change.split())
    nownum = nownum + Change[1] - Change[0]
    largest.append(nownum)

print max(largest)
