case = int(input())

for _ in range(case):
    n, m = map(int, input().split())
    queue = list(map(int, input().split()))
    queue = list((i, v) for i, v in enumerate(queue))
    answer = 0

    while True:
        if queue[0][1] == max(queue, key=lambda x:x[1])[1]:
            answer += 1
            if queue[0][0] == m:
                print(answer)
                break
            else:
                queue.pop(0)
        else:
            queue.append(queue.pop(0))

