for i in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    hotel = []
    
    for _ in range(N):    
        *l, name = input().split()
        # bed_size, room_capacity, num_rooms, price, hotel_name
        hotel.append([*map(int, l)] + [name])
    
    team = []
    
    for _ in range(M):
        bed_size_type, *l = input().split()
        team.append([bed_size_type] + [*map(int, l)])
        # bed_size_type, people_num, max_person_per_room
    
    print(f'Case #{i}:')
    
    for bed_size_type, people_num, max_person in team:
        temp = []
        for bed_size, room_capacity, room_num, price, name in hotel:
            # 침대 크기 타입에 따른 범위 설정
            bed_range_min = {'A': 20, 'B': 36, 'C': 49}[bed_size_type]
            bed_range_max = {'A': 35, 'B': 48, 'C': 62}[bed_size_type]
            
            if bed_range_min <= bed_size <= bed_range_max:
                # 팀이 요구하는 방 개수 계산
                people_per_room = min(max_person, room_capacity)
                required_rooms = (people_num + people_per_room - 1) // people_per_room
                
                if room_num >= required_rooms:  # 방이 충분한지 확인
                    total_cost = required_rooms * price
                    temp.append([total_cost, bed_size, name])
        
        if temp:
            # 가격이 가장 저렴한 호텔 선택, 가격이 같으면 침대 크기, 그것도 같으면 리스트의 순서대로
            best_hotel = min(temp, key=lambda x: (x[0], -x[1]))
            print(best_hotel[0], best_hotel[2])
        else:
            print('no-hotel')