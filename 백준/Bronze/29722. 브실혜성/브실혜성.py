p,q,r=map(int,input().split('-'))
t=p*360+~-q*30+r+int(input())-1
print(f'{t//360}-{t//30%12+1:02}-{t%30+1:02}')