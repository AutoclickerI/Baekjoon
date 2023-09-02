n,c,h=map(int,input().split())
for _ in[0]*n:
    t=int(input())
    if t>h:
        h=t
        print(f'BBTV: Dollar reached {h} Oshloobs, A record!')
    elif c>t:
        print(f'NTV: Dollar dropped by {c-t} Oshloobs')
    c=t