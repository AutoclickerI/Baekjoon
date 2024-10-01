import math

def round_price(price):
    """Round price to 2 decimal places, rounding up from 0.005"""
    return math.floor(price * 100 + 0.5) / 100

def main():

    # Read first line for robot count, initial price, and target day
    first_line = input().split()
    N = int(first_line[0])
    P_0 = float(first_line[1])
    T = int(first_line[2])

    # Read robot parameters
    robots = []
    for i in range(1, N + 1):
        S_i, I_i, M_i = input().split()
        robots.append((int(S_i), int(I_i), float(M_i)))

    # Prices array - initializing all prices to None except the first robot on day 0
    prices = [[None] * (T + 1) for _ in range(N)]
    prices[0][0] = P_0  # Robot 1 starts with price P_0 on day 0

    # Simulate day-by-day
    for day in range(1, T + 1):
        for idx in range(N):
            S_i, I_i, M_i = robots[idx]

            # Check if the robot should make a new offer today
            if day >= S_i and (day - S_i) % I_i == 0:
                # Calculate the average price of all active offers from the previous day
                active_prices = [prices[j][day - 1] for j in range(N) if prices[j][day - 1] is not None]
                if active_prices:
                    avg_price = sum(active_prices) / len(active_prices)
                    new_price = avg_price * (1 + M_i)
                    prices[idx][day] = round_price(new_price)
            else:
                # Carry forward the previous day's price if no update is made
                prices[idx][day] = prices[idx][day - 1]

    # Output the prices at the start of day T
    for idx in range(N):
        print(f"{prices[idx][T - 1]:.2f}")

if __name__ == "__main__":
    main()