c=input().count
for i in 0,1,2,3:print((i^c('H')*2+c('V')%2&3)+1)