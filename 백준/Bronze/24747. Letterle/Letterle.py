s=input()
for j in range(7):
    p=input()
    s==p<exit(print('WINNER'))
    j==6<exit(print('LOSER'))
    for i,j in zip(p,s):print(end='G'*(i==j)or'Y'*(i in s)or'X')
    print()