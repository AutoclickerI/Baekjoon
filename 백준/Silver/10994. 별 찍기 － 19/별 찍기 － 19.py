a=['*']
n=int(input())-1
for i in range(n):
    b=['*'*(4*i+5),'*'+' '*(4*i+3)+'*']
    for p in a:
        b.append('* '+p+' *')
    b+=['*'+' '*(4*i+3)+'*','*'*(4*i+5)]
    a=b
print(*a,sep='\n')