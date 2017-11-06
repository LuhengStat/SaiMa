s = raw_input()
s = map(int, s.split())

out = (s[0]+s[1])/(s[0]+0.0)
print "%.1f" % out

