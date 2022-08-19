n = int(input())
sort_list = list(map(int, str(n)))
def merge_sort(sort_list):
    if len(sort_list) <= 1:
        return sort_list
    mid = len(sort_list) // 2
    front_arr = merge_sort(sort_list[:mid])
    back_arr = merge_sort(sort_list[mid:])
    # print("f", front_arr, "b", back_arr)
    merged_arr = []
    f = b = 0
    while f < len(front_arr) and b < len(back_arr): # 좌우 비교해서 작은것부터 넣어줌
        if front_arr[f] > back_arr[b]:
            merged_arr.append(front_arr[f])
            f += 1
        else:
            merged_arr.append(back_arr[b])
            b += 1
    merged_arr += front_arr[f:] # 나머지 것들 넣어줌
    merged_arr += back_arr[b:]
    return merged_arr

answer = "".join(map(str, merge_sort(sort_list)))

print(answer)