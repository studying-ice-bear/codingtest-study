def solution(arr):
    answer = -1
    n = (len(arr) + 1) // 2
    INF = int(10e9)
    dp_min = [[INF] for _ in range(n) for _ in range(n)]
    dp_max = [[-INF] for _ in range(n) for _ in range(n)] 
    
    for i in range(0, len(arr), 2):
        dp_min[i // 2][i // 2] = arr[i]
        dp_max[i // 2][i // 2] = arr[i]
    
    
        
    return answer