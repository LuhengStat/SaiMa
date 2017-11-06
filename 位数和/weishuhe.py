n = int(raw_input())
n = int(n)

def fun(n):
    ori = n
    if n <= 2:
        return n
    out = [2, 1]
    n = n-3
    while n> 0:
        if n - 3 >= 0:
            out.append(2)
            out.append(1)
            n = n-3
        else:
            if n == out[len(out)-1]:
                out[0] = out[0] + n
                n=0
            else:
                out.append(n)
                n = 0
    return out

out = fun(n)
outstr = map(str, out)
out = "".join(outstr)
out = int(out)

print out