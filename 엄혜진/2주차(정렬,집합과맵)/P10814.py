N = int(input())

members = []

for i in range(N):
    age, name = input().split()
    members.append([int(age), name, i])

members.sort(key=lambda x: [x[0], x[2]])

for member in members:
    print(member[0], member[1])