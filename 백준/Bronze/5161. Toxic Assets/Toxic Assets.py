def solve():
    K = int(input())  # Number of data sets
    for dataset in range(1, K + 1):
        B, D = map(int, input().split())  # B: number of basic investments, D: number of derivatives
        basic_values = list(map(float, input().split()))  # Current values of basic investments

        # To store values of both basic investments and derivatives
        values = basic_values[:]

        # Now we read the derivatives and compute their values
        for d in range(D):
            # Read the percentages for the current derivative
            percentages = list(map(float, input().split()))

            # Compute the value of the current derivative B+d
            value = 0
            for i, percentage in enumerate(percentages):
                value += percentage * values[i]
            values.append(value)

        # Now read the portfolio distribution
        portfolio_distribution = list(map(float, input().split()))

        # Calculate the current value of the portfolio
        portfolio_value = 0
        for i in range(B + D):
            portfolio_value += portfolio_distribution[i] * values[i]

        # Output the result for the current dataset
        print(f"Data Set {dataset}:")
        print(f"{portfolio_value:.2f}")
        print()

# Call the function to solve the problem
solve()