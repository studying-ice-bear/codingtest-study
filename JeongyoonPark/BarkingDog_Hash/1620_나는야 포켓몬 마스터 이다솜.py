import sys
input = sys.stdin.readline

n, m = map(int, input().split())

pokemon_name = {}
for i in range(n):
    pokemon_name[i+1] = input().rstrip()

pokemon_name_2 = {v : k for k, v in pokemon_name.items()}

for i in range(m):
    word = input().rstrip()
    if word.isalpha():
        print(pokemon_name_2.get(word))
    else:
        print(pokemon_name.get(int(word)))