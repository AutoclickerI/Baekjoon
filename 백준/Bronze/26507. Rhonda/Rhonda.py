def print_grid(grid):
    for row in grid:
        print(" ".join(f"{cell:02d}" for cell in row))

def main():
    # Read number of layers
    i = int(input())
    
    # Read each 10x10 layer and store it in a list
    layers = []
    for _ in range(i):
        layer = [list(map(int, input().strip())) for _ in range(10)]
        layers.append(layer)
        input()
    
    # Read number of datasets
    n = int(input())
    
    # Process each dataset
    for _ in range(n):
        # Read the indices of the layers to combine
        dataset = list(map(int, input().split()))
        
        # Initialize a 10x10 grid with zeros
        result_grid = [[0] * 10 for _ in range(10)]
        
        # Sum the corresponding cells from the selected layers
        for layer_idx in dataset:
            for r in range(10):
                for c in range(10):
                    result_grid[r][c] += layers[layer_idx][r][c]
        
        # Print the result grid
        print_grid(result_grid)
        print()

# Call the main function to execute the program
if __name__ == "__main__":
    main()