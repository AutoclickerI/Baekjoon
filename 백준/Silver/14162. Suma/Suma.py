L,R=map(int,input().split())
print(sum(i*(R//i+L//-i+1)for i in range(1,R+1)))