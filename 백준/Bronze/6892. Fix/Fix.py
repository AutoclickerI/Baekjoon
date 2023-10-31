def f(a,b,c):
    return a.startswith(b)or a.endswith(b)or a.startswith(c)or a.endswith(c)
for _ in[0]*int(input()):
    a,b,c=input(),input(),input()
    print('YNeos'[f(a,b,c)or f(b,a,c)or f(c,a,b)::2])