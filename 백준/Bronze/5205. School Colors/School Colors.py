import math

def euclidean(c1, c2):
    return math.sqrt((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2 + (c1[2]-c2[2])**2)

K = int(input())
for dataset_index in range(1, K+1):
    n = int(input())
    colors = [tuple(map(int, input().split())) for _ in range(n)]

    max_contrast = -1
    best_pairs = []

    for i in range(n):
        for j in range(i+1, n):
            contrast = euclidean(colors[i], colors[j])
            if contrast > max_contrast:
                max_contrast = contrast
                best_pairs = [(i+1, j+1)]
            elif contrast == max_contrast:
                best_pairs.append((i+1, j+1))

    best_pairs.sort()  # lexicographic sort by (i, j)

    print(f"Data Set {dataset_index}:")
    for a, b in best_pairs:
        print(f"{a} {b}")
