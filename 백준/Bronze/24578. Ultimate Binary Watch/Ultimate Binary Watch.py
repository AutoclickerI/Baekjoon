s=input()
for i in 8,4,2,1:a,b,*c=['.*'[int(j)&i>0]for j in s];print(a,b,' ',*c)