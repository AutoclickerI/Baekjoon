a,b,c,d,e,f,g,h=map(int,input().split())
print(max((a-c)**2+(b-d)**2,(e-g)**2+(f-h)**2)**0.5)