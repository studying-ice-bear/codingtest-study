def hanoi(n, one, three, two):
    if n == 1:  # 원반 한 개를 옮기는 문제면 그냥 옮기면 됨
        print(one, "->", three)
        return

    # 원반 n - 1개를 aux_pos로 이동(to_pos를 보조 기둥으로)
    hanoi(n - 1, one, two, three) # 첫번째 에있는
    # 가장 큰 원반을 목적지로 이동
    print(one, "->", three)
    # aux_pos에 있는 원반 n-1개를 목적지로 이동(from_pos를 보조 기둥으로)
    hanoi(n - 1, two, three, one)

hanoi(2, 1, 3, 2)

n = input() # 장대에 쌓인 원판의 개수