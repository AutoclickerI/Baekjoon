N = int(input())
card_set = {1:0, 2:0, 3:0, 4:0}

def getWinner(A, B) :
    for i in range(4, 0, -1) :
        if A[i] > B[i] :
            return print("A")
        elif A[i] < B[i] :
            return print("B")
    return print("D")

for _ in range(N) :
    A = card_set.copy()
    B = card_set.copy()
    a_card_list = list(map(int, input().split()))[1::]
    b_card_list = list(map(int, input().split()))[1::]

    for card in a_card_list :
        A[card] += 1
    for card in b_card_list :
        B[card] += 1

    getWinner(A, B)