while 1:
    n=input()
    p=0
    if n=='0':
        break
    for i in range(len(n)):
        if n[i]!=n[-1-i]:
            p=1
    print('yes'if p==0 else 'no')