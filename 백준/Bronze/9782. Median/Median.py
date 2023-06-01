j=1
while(i:=input())!='0':n,*l=map(int,i.split());print(f'Case {j}: {l[n//2]if n%2 else (l[n//2-1]+l[n//2])/2:.1f}');j+=1