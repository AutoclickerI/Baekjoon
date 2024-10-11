for _ in[0]*int(input()):
    d={i:['0']*100for i in'rgby'}
    M=int(input())
    for i in input().split():n,c=int(i[:-1])-1,i[-1];d[c][n] = '1'
    print('NYOE S'[any('111'in''.join(c)for c in d.values())or any(l.count('1')>2for l in zip(*d.values()))::2])