n, m = map(int, input().split())
card_list = sorted(list(map(int, input().split())), reverse = True)
limit = 0
result = 0

for i in range(len(card_list)):
    for j in range(i+1, len(card_list)):
        for k in range (j+1, len(card_list)):
            limit = card_list[i]+card_list[j]+card_list[k]
            if limit <=m:
                result = max(result, limit)

print(result)