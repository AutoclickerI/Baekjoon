I=input
for t in range(int(I())):s=I();l,r=map(int,I().split());print(f'Case #{t+1}:',(s*(r//len(s)+1))[l-1:r].count('B'))