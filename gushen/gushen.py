s = raw_input()
s = int(s)

def Pos(s):
    out = (-1 + (1 + ((8*s)**(1/2.0))))
    out = int(out/2)
    if out*(out+1)/2.0 >= s:
        return out
    else:
        return out+1


def assetreturn(n):
    pos = Pos(n)
    if pos*(pos+1)/2.0 == n:
        return 1 + (pos-2)*(pos-1)/2
    else:
        return 1 + (pos-3)*(pos-2)/2 + (n-pos*(pos-1)/2)

def allreturn(n):
    out = range(n)
    for i in range(1, n+1):
        out[i-1] = assetreturn(i)
    return out

print assetreturn(s)