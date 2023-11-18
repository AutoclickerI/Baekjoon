s=''
for i in range(int(input())):i=str(i+1);s+=i*-~-(i in s)
print(s)