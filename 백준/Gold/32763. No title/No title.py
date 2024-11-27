N=int(input())
l=[1]
for i in range(N-1):
    print(f'? {i+1} * {i+2}')
    if input()=='+':
        l+=l[-1],
    else:
        l+=1-l[-1],
if 1 in l[1:]:
    idx=l.index(1,1)
    print(f'? 1 + {idx+1}')
    if input()=='-':
        l=[1-i for i in l]
else:
    print('? 2 + 3')
    if input()=='+':
        l=[1-i for i in l]
print('!',*['-+'[i]for i in l])