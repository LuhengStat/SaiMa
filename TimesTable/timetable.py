
s = raw_input()
s = map(int, s.split())

def timetable(m, n, k):
    alltable = []
    if k < m or k < n:
        return k
    for i in range(1, m+1):
        alltable = alltable + [item*i for item in range(1, n+1)]
    alltable = sorted(alltable)
    return alltable[k-1]

print timetable(s[0], s[1], s[2])

