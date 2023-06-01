f=lambda:len(input().strip())
s=lambda:f'{f()}:{f()}:{f()}'
print('Latitude',s(),'Longitude',s())