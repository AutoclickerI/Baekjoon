import math
i=1
while'1'<(s:=input()):w,d=map(int,s.split());y=int(math.log(810*w/d,2)*5730);print(f'Sample #{i}\nThe approximate age is {round(y,-3+(y<10000))} years.\n');i+=1