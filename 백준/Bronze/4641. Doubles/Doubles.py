while a:=input().split()[:-1]:print(sum(str(int(i)*2)in a for i in a))