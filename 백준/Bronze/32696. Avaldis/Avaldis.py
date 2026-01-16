A,B=map(int,input().split())
print([B,str(A)[:A*A-2]+'x'+'%+d'%B*(B!=0)][A!=0])