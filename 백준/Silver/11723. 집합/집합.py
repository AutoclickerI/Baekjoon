import sys
d=0
for _ in range(int(input())):
    l=sys.stdin.readline().split()
    if l[0]=='add':d|=1<<int(l[1])
    elif l[0]=='check':print((d>>int(l[1]))%2)
    elif l[0]=='remove':d&=4194303-(1<<int(l[1]))
    elif l[0]=='toggle':d^=1<<int(l[1])
    elif l[0]=='all':d=4194303
    else:d=0