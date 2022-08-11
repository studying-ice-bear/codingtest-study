import sys

N = int(sys.stdin.readline().rstrip())

cards = {}

numbers = list(map(int, sys.stdin.readline().rstrip().split()))
for number in numbers:
    if number in cards:
        cards[number] += 1
    else:
        cards[number] = 1

M = int(sys.stdin.readline().rstrip())

quests = list(map(int, sys.stdin.readline().rstrip().split()))
for quest in quests:
    result = cards.get(quest)
    if result == None:
        sys.stdout.write(str(0) + ' ')
    else:
        sys.stdout.write(str(result) + ' ')