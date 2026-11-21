Y,c=map(int,input().split())
print(f"SN {Y}{chr(64+c)*(c<27)or'%c%c'%(96+~-c//26,97+~-c%26)}")