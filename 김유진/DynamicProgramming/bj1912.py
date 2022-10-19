import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
memory = [0] * n

memory[0] = arr[0]
for i in range(1, n):
    memory[i] = max(memory[i-1] + arr[i], arr[i])

print(max(memory))
