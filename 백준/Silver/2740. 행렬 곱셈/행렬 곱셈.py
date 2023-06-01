mat1=[[*map(int,input().split())]for _ in[0]*[*map(int,input().split())][0]]
mat2=[[*map(int,input().split())]for _ in[0]*[*map(int,input().split())][0]]
def matmul(m1,m2):
    return [[sum(m1[i][k]*m2[k][j]for k in range(len(m2)))for j in range(len(m2[0]))]for i in range(len(m1))]
[print(*i)for i in matmul(mat1,mat2)]