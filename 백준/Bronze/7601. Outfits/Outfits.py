s=1
while'1'<(i:=input()):
 n,d=map(int,i.split())
 a,b=eval('int(input())or 1e3,'*2);print(f'Scenario {s}');s+=1
 for i in range(d):c,d=map(int,input().split());print(f'Day {i+1} {["OK","ALERT"][c+(c>=a)==n-d+1-(d>=b)]}')