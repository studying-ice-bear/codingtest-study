import sys
N = int(sys.stdin.readline())
memory = [0] * (N+1)

for i in range(2, N+1):
    memory[i] = memory[i-1] + 1

    if i % 3 == 0:
        memory[i] = min(memory[i], memory[i // 3] + 1)

    if i % 2 == 0:
        memory[i] = min(memory[i], memory[i // 2] + 1)


print(memory[N])
