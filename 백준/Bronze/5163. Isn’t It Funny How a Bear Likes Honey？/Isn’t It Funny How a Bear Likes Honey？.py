for i in range(int(input())):
    b,w=map(eval,input().split())
    print(f'Data Set {i+1}:\n{"YNeos"[sum(4*3.14159265358979323846/3*eval(input())**3for _ in[0]*b)<w*1000::2]}\n')