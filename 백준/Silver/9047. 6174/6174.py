for _ in[0]*int(input()):
    n=int(input())
    c=0
    while n!=6174:
        s=''.join(sorted(f'{n:04d}'))
        n=int(s[::-1])-int(s)
        c+=1
    print(c)