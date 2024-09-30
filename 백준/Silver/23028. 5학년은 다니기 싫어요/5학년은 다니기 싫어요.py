a,b,c=map(int,input().split())
for i in range(8-a):j,g=map(int,input().split());b+=3*j;c+=3*min(6,j+g)
print(['Nae ga wae','Nice'][b>65<129<c])