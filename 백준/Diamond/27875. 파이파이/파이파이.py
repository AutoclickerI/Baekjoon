s=lambda i,d:sum(pow(16,d-j,(8*j+i)**2)/(8*j+i)**2 for j in range(d+1))+sum(16**(d-j)/(8*j+i)**2 for j in range(d+1,d+9))

n=int(input())-1
print(hex((int(16*(16*s(1,n)-16*s(2,n)-8*s(3,n)-16*s(4,n)-4*s(5,n)-4*s(6,n)+2*s(7,n)))+15)%16).upper()[2:])