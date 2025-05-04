import re
r=[[i[:-3],[*map(lambda i:int(i)*64,i[-3:])]] for i in re.findall('.+?\d+','White444Silver333Gray222Black000Red400Maroon200Yellow440Olive220Lime040Green020Aqua044Teal022Blue004Navy002Fuchsia404Purple202')]
f=lambda x,y,z:(x-a)**2+(y-b)**2+(z-c)**2
for i in[*open(0)][:-1]:a,b,c=map(int,i.split());print(min(r,key=lambda i:f(*i[1]))[0])