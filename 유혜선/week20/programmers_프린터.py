from collections import deque as dq

def solution(priorities, location):
    wait_q = dq([(val, idx) for idx, val in enumerate(priorities)])
    i = 0
    
    while wait_q:
        val_j, idx_j = wait_q.popleft()
        
        if max(wait_q)[0] > val_j:
            wait_q.append((val_j, idx_j))
        else:
            i += 1
            if idx_j == location:
                return i



print(solution([2, 1, 3, 2], 2), 1)
print(solution([1, 1, 9, 1, 1, 1], 0), 5)