"""
문제 > https://school.programmers.co.kr/learn/courses/30/lessons/42579?language=python3
규칙 >
속한 노래가 많이 재생된 장르를 먼저 수록
그중에서 가장 많이 재생된 노래를 두 개 수록
재생횟수가 같으면 고유번호가 낮은 노래를 수록

아이디어 > 
장르의 총 재생 횟수를 저장하는 dict와 장르별 곡 인덱스와 횟수를 저장하는 dict를 이용해서
1) 장르별 총 재생횟수가 높은 순서대로 정렬하고
2) 장르별 곡들의 횟수가 높고 인덱스는 낮은 순서대로 정렬해서
3) 장르별로 두 곡씩 answer 배열에 집어넣는다.
"""

def solution(genres, plays):
    answer = []
    n = len(genres)
    process_g = {genre: 0 for genre in set(genres)}
    process_p = {genre: [] for genre in set(genres)}
    for i in range(n):
        process_g[genres[i]] += plays[i]
        process_p[genres[i]].append([plays[i], i])
    
    popular_genres = sorted(process_g.items(), key=lambda x: x[1], reverse=True)
    for i in range(len(popular_genres)):
        genre = popular_genres[i][0]
        songs = process_p[genre]
        songs.sort(key=lambda x: x[0], reverse=True)
        
        answer.append(songs[0][1])
        if len(songs) > 1:
            answer.append(songs[1][1])
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))