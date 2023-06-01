p,q=map(int,input().split())
t=p*60+q
t-=int(input())
p,q=map(int,input().split())
t-=p*60+q
t-=(int(input())+1)*int(input())+10
print(f'{t//60:02d} {t%60:02d}')