print(*sorted(range(1,n:=int(input())+1),key=lambda x:(n-x&2)*-x))