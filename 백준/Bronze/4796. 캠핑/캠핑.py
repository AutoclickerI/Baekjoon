c=0
while(s:=input())>'1':
    L,P,V=map(int,s.split())
    c+=1
    print(f'Case {c}:',min(V%P,L)+V//P*L)