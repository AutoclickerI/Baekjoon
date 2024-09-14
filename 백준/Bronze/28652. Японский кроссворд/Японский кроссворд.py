def p(l):
    for i in l:
        s=i.replace(*'. ').split()
        print(len(s),*map(len,s))
H,W=map(int,input().split())
l=eval('input(),'*H)
p(l)
print()
p(map(''.join,zip(*l)))