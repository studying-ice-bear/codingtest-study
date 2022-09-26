def solution(priorities, location):
    answer_list = [] # 중요도 순서대로 완성된 리스트 [1,2,3]  => [+3+2+1]
    p_list = [i for i in range(len(priorities))] # 인쇄 인덱스 저장하는 리스트 [0,1,2]
    
    while(len(priorities) != 0):  # pop으로 계속 삭제 해서 리스트 길이가 0이 될 떄 까지
        if priorities[0] == max(priorities): # 중요도 리스트 첫 번째가 제일 중요도가 높을 때 [3,2,1]
            answer_list.append(p_list.pop(0)) # answer_list 에 넣어주고 삭제 
            priorities.pop(0) [2,1]
        else:
            priorities.append(priorities.pop(0)) # 아니라면 첫번째를 맨 뒤로 보내고 [1,2,3] -> [2,3,1] -> [3,1,2] 
            p_list.append(p_list.pop(0)) #똑같이 첫번쨰 를 맨 뒤로 [0,1,2] -> [1,2,0] -> [2,0,1]
    return answer_list[location] + 1       
            
            
# 도중
        
        
        