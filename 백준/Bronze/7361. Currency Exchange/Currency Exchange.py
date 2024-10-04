def round_to_cents(amount):
    return round(amount * 100 + 0.00001) / 100

def process_trips(exchange_rates, trips):
    results = []
    for trip in trips:
        # Extract trip details
        n = trip[0]
        if n == 0:
            break
        countries = trip[1:-1]
        initial_amount = trip[-1]

        # Start with the initial amount of US dollars
        amount = initial_amount

        # Perform exchanges through the trip
        current_country = 1  # Start with US dollars
        for next_country in countries:
            amount *= exchange_rates[current_country - 1][next_country - 1]
            amount = round_to_cents(amount)
            current_country = next_country

        # Finally, convert back to US dollars (country 1)
        amount *= exchange_rates[current_country - 1][0]
        amount = round_to_cents(amount)

        # Store the result
        results.append(f"{amount:.2f}")
    
    return results

# Input parsing
exchange_rates = []
for _ in range(5):
    exchange_rates.append(list(map(float, input().split())))

trips = []
while True:
    trip = input().split()
    if len(trip) == 1 and trip[0] == '0':
        break
    trips.append([int(x) if i < len(trip) - 1 else float(x) for i, x in enumerate(trip)])

# Process trips and output results
results = process_trips(exchange_rates, trips)
for result in results:
    print(result)
