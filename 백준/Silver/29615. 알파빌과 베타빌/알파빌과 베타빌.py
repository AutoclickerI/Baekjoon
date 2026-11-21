N,M=map(int,input().split())
l=input().split()
s={*input().split()}
print(sum(i not in s for i in l[:M]))