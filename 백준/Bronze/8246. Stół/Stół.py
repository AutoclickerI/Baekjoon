w,h,k=map(int,input().split())
w//=k
h//=k
print(w*h-max(0,w-2)*max(0,h-2))