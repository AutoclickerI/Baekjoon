stack=[]
for i in input():
    stack+=i,
    while stack[-4:]==[*'PPAP']:
        del stack[-3:]
if stack==['P']:print('PPAP')
else:print('NP')