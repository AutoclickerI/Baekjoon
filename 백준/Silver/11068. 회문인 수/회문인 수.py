def to_b(n,b):
    if n<b:
        return[n]
    return to_b(n//b,b)+[n%b]

for i in[*open(0)][1:]:
    n=int(i)
    print(+any(to_b(n,b)==to_b(n,b)[::-1]for b in range(2,65)))