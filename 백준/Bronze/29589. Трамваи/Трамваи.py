def get_tram_numbers(n, m, k, tram_times, passenger_times):
    tram_index = 0
    tram_capacity = 0
    result = [-1] * m
    waiting_queue = []
    
    passenger_ptr = 0
    for tram_index in range(n):
        current_tram_time = tram_times[tram_index]
        tram_capacity = k

        # Board passengers from the queue first if any
        while waiting_queue and tram_capacity > 0:
            passenger_index = waiting_queue.pop(0)
            result[passenger_index] = tram_index + 1
            tram_capacity -= 1
        
        # Board passengers arriving at the current tram time or before the next tram
        while passenger_ptr < m and passenger_times[passenger_ptr] <= current_tram_time:
            if tram_capacity > 0:
                result[passenger_ptr] = tram_index + 1
                tram_capacity -= 1
            else:
                waiting_queue.append(passenger_ptr)
            passenger_ptr += 1
    
    # Process remaining passengers in the queue
    while tram_index < n - 1:
        tram_index += 1
        tram_capacity = k
        while waiting_queue and tram_capacity > 0:
            passenger_index = waiting_queue.pop(0)
            result[passenger_index] = tram_index + 1
            tram_capacity -= 1

    return result

# Read input
n, m, k = map(int, input().split())
tram_times = [input().strip() for _ in range(n)]
passenger_times = [input().strip() for _ in range(m)]

# Convert time format hh:mm to minutes since start of day
def time_to_minutes(time):
    hh, mm = map(int, time.split(':'))
    return hh * 60 + mm

tram_times = [time_to_minutes(t) for t in tram_times]
passenger_times = [time_to_minutes(t) for t in passenger_times]

# Get the tram numbers each passenger boards
result = get_tram_numbers(n, m, k, tram_times, passenger_times)

# Print results
for res in result:
    print(res)