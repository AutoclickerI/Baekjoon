l=b'5HJ<2B>@4G=D76?FM:839A;IKL'
for T in range(int(input())):
    s=''
    for i in input().split():
        s+=chr(65+l.index(48+int('1'+i.translate({46:48, 45:49}),2)))
    print(f'Case {T+1}:',s)