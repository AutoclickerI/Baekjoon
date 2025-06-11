l=[5,24,26,12,2,18,14,16,4,23,13,20,7,6,15,22,29,10,8,3,9,17,11,25,27,28]
for T in range(int(input())):
    s=''
    for i in input().split():
        s+=chr(65+l.index(int('1'+i.translate({46:48, 45:49}),2)))
    print(f'Case {T+1}:',s)