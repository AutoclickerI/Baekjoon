def mem(s):
    if len({*s})==1or[*s]==sorted(s)and len(s)==len({*s}):
        return 1
    return 0
l=[i for _ in[0]*int(input())if mem(i:=input())]
print(min(l,key=int)if l else'NERASTA')