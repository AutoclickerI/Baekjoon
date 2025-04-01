import sys
import itertools

def canonical_edges(m, edges):
    # Store each edge as a sorted tuple (min, max)
    return {tuple(sorted((u, v))) for u, v in edges}

def is_isomorphic(g1_edges, g2_edges):
    # All vertices for graphs of 3 vertices
    vertices = [1, 2, 3]
    for perm in itertools.permutations(vertices):
        # Build a mapping: original -> permuted value
        mapping = {original: perm[i] for i, original in enumerate(vertices)}
        mapped_edges = {tuple(sorted((mapping[u], mapping[v]))) for u, v in g1_edges}
        if mapped_edges == g2_edges:
            return True
    return False

def main():
    input_data = sys.stdin.read().strip().split()
    it = iter(input_data)
    T = int(next(it))
    results = []
    for _ in range(T):
        m1 = int(next(it))
        edges1 = []
        for _ in range(m1):
            u = int(next(it))
            v = int(next(it))
            edges1.append((u, v))
        g1_edges = canonical_edges(m1, edges1)
        
        m2 = int(next(it))
        edges2 = []
        for _ in range(m2):
            u = int(next(it))
            v = int(next(it))
            edges2.append((u, v))
        g2_edges = canonical_edges(m2, edges2)
        
        if is_isomorphic(g1_edges, g2_edges):
            results.append("yes")
        else:
            results.append("no")
    
    print("\n".join(results))

if __name__ == '__main__':
    main()
