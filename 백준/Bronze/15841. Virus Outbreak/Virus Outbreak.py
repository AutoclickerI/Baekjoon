a=[0,1]
exec('a+=a[-1]+a[-2],;'*500)
while~(n:=int(input())):print('Hour %d:'%n,a[n],'cow(s) affected')