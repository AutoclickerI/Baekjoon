v=eval(input().replace(*' /'))
print(['very strong'[(v<.6)*5:],'normal','weak'][(v<.2)+(v<.4)])