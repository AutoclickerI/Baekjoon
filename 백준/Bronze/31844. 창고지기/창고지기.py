x,y,z=map(input().find,'@#!')
print(abs(z-x)*((x<y)^(y>z))-1)