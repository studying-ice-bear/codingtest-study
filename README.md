# 공부하는 아이스베어 코테스터디

## 목표

- 매주 2개의 카테고리([바킹독 공개문제집 (221114 변경)](https://www.acmicpc.net/workbook/by/BaaaaaaaaaaarkingDog) ~~[백준 단계별로 풀기(220808 - 221114)](https://www.acmicpc.net/step)~~) 안에서 문제 최소 5개씩 풀기
- 매주 월요일 8시에 스터디 모임
  1. 코드 공유 (약 1시간)
     - 무조건 1문제를 설명한다. 설명할 문제가 겹쳐도 무관하다.
  2. 랜덤으로 고른 문제 1개를 다같이 풀고, 푼 방법 공유 (약 30분)
     - [프로그래머스 고득점 Kit](https://school.programmers.co.kr/learn/challenges?tab=algorithm_practice_kit)에서 랜덤으로 결정함.

## 기간

2022.08.08 ~ 

## 기록

### 0808 

- 카테고리: [재귀](https://www.acmicpc.net/step/19), [브루트 포스](https://www.acmicpc.net/step/22)
- 랜덤문제: 재귀의 [하노이 탑 이동순서](https://www.acmicpc.net/problem/11729)

### 0815 

> 공휴일에도 스터디하는 사람 성공한대요~

- 카테고리: [정렬](https://www.acmicpc.net/step/9), [집합과 맵](https://www.acmicpc.net/step/49)
- 랜덤문제: [해시](https://school.programmers.co.kr/learn/courses/30/parts/12077)의 [베스트 앨범](https://school.programmers.co.kr/learn/courses/30/lessons/42579)


### 0822

- 카테고리: [백트랙킹](https://www.acmicpc.net/step/34), [동적계획법1](https://www.acmicpc.net/step/16)
  - 출제 빈도를 고려하여(~~스터디원 뇌피셜~~) 기하1과 정수론과 조합론은 스터디에서 진행하지 않기로 함.
  - 의논한 문제
    - [N-queen](https://www.acmicpc.net/problem/9663)
      - 힌트: 충돌하지 않게 위치시키려면 같은 행 또는 열을 배제해야 하기때문에, 1차원배열에 저장해도 된다(2차원 배열이 없어도 표현 가능하다.)
        - 예를 들어, ```[0, 2, 3, 1]```는 1행 2열, 2행 3열, 3행 1열에 퀸이 위치한다는 의미.
    - [포도주 시식](https://www.acmicpc.net/problem/2156)
      - 계단 오르기와 비슷하지만 시작점과 끝점이 없다는 것이 다르다.
      - 해결 못한 반례 (해결했다면 '질문'채널에 설명 남겨주기~)
        ```
        답 : 36
        Input:
        10
        0
        0
        10
        0
        5
        10
        0
        0
        1
        10
        ```
- 랜덤문제: [스택/큐](https://school.programmers.co.kr/learn/courses/30/parts/12081)의 [같은 숫자는 싫어](https://school.programmers.co.kr/learn/courses/30/lessons/12906)
  - 다들 푼 방식이 비슷하고, 배열이나 큐를 사용해서 풀었다.
  - 프로그래머스에서 파이써닉하게 푼 것도 신기했음 
    ```python
    return  [arr[i] for i in range(len(arr)) if not(arr[i:i+1] == arr[i+1:i+2])]
    ```
  - 자바스크립트로 filter를 사용해서 한 줄에 나타낸 코드가 있었음
    ```javascript
    return arr.filter((val,index) => val != arr[index+1]);
    ```


### 0829

- 카테고리: [누적합](https://www.acmicpc.net/step/48), [그리디 알고리즘](https://www.acmicpc.net/step/33)
  - 의논한 문제
    - [나머지 합](https://www.acmicpc.net/problem/10986)
      - 힌트: 누적 합의 나머지를 구하고 그 값이 같은 것끼리 그룹을 형성한다. 각 그룹에서 2개를 고르면(조합) 범위가 형성된다. 나머지가 같기 때문에 두 값의 차가 0이라서, 최종적으로 누적합을 M으로 나누면 0이 된다.
- 랜덤문제: [힙](https://school.programmers.co.kr/learn/courses/30/parts/12117)의 [더 맵게](https://school.programmers.co.kr/learn/courses/30/lessons/42626)
  - 모두 [heapq](https://docs.python.org/ko/3/library/heapq.html) 사용해서 문제를 풀었다.
  - 우성님이 소개해 준 함수
    - [all(iterable)](https://docs.python.org/ko/3/library/functions.html?highlight=all#all): iterable 요소가 모두 참이면 True 반환
    - [any(iterable)](https://docs.python.org/ko/3/library/functions.html?highlight=all#any): iterable 요소가 하나라도 참이면 True 반환


### 0905

- 카테고리: [스택](https://www.acmicpc.net/step/11), [큐, 덱](https://www.acmicpc.net/step/12)
  - 의논한 문제
    - [스택 수열](https://www.acmicpc.net/problem/1874)
    - [오큰수](https://www.acmicpc.net/problem/17298)
- 랜덤문제: [정렬](https://school.programmers.co.kr/learn/courses/30/parts/12198)의 [가장 큰 수](https://school.programmers.co.kr/learn/courses/30/lessons/42746)


#### 0912 

- 추석연휴로 쉬어가기


### 0919

- 카테고리: [분할정복](https://www.acmicpc.net/step/20), [이분탐색](https://www.acmicpc.net/step/29)
  - 의논한 문제
    - [랜선 자르기](https://www.acmicpc.net/problem/1654): 각 랜선을 특정 개수로 똑같이 자를 때 최대 길이 구하기
    - [행렬제곱](https://www.acmicpc.net/problem/10830)
      - 4시간을 투자한 혜선님의 조언: 나머지를 구하는 문제인데 시간초과를 만났다면 ⭐ 모듈러 연산 ⭐ 사용하기
        1. (a + b) mod n = ((a mod n) + (b mod n)) mod n
        2. (a - b) mod n = ((a mod n) - (b mod n)) mod n
        3. (a * b) mod n = ((a mod n) * (b mod n)) mod n
      - [곱셈](https://www.acmicpc.net/problem/1629)이랑 유사하다.
- 랜덤문제: [완전탐색](https://school.programmers.co.kr/learn/courses/30/parts/12230)의 [모음사전](https://school.programmers.co.kr/learn/courses/30/lessons/84512)

### 0926

- 카테고리: [우선순위 큐](https://www.acmicpc.net/step/13), [동적계획법2](https://www.acmicpc.net/step/17)
- 랜덤문제: [탐욕법](https://school.programmers.co.kr/learn/courses/30/parts/12244)의 [조이스틱](https://school.programmers.co.kr/learn/courses/30/lessons/42860)
  - 아무도 못 풀었다🥲. 알파벳보다는 이동횟수 계산이 이 문제의 핵심인것 같다.
 
### 1003

- 카테고리: [동적계획법1](https://www.acmicpc.net/step/16), [동적계획법2](https://www.acmicpc.net/step/17)
- 랜덤문제: [동적계획법](https://school.programmers.co.kr/learn/courses/30/parts/12263)의 [사칙연산](https://school.programmers.co.kr/learn/courses/30/lessons/1843) 
  - 아무도 못 풀었다🥲. 다음주 스터디 시간까지 풀거나 공부해서 설명하기로 함.
  
### 1010

- 지난 주에 못푼 문제 사칙연산 풀이방법 의논
  - [1안: 2차원 배열에서 해결](https://school.programmers.co.kr/questions/35224)
  - [2안: 1차원 배열에서 해결](https://tiktaek.tistory.com/33)
- 카테고리: [그래프와 순회](https://www.acmicpc.net/step/24)
  - [뱀과 사다리 게임](https://www.acmicpc.net/problem/16928)
  - JS로 문제 풀 때 자료구조 Map을 사용해서 풀었음
    - [JS에서 Set, Map, Object 차이](https://velog.io/@proshy/JSSet-Map-Object-%EC%A0%95%EB%A6%AC)
  - 파이썬으로 dfs 문제 풀 때, 재귀호출 제한을 따로 설정해야 했음. (Python3 기준으로 최대 재귀 깊이는 1000)
    ```python
    import sys

    sys.setrecursionlimit(10 ** 9)
    ```
  - dfs 문제 풀 때, 재귀 또는 스택으로 푸는 방법이 있음
- 랜덤문제: [깊이/너비 우선탐색(DFS/BFS)](https://school.programmers.co.kr/learn/courses/30/parts/12421)의 [네트워크](https://school.programmers.co.kr/learn/courses/30/lessons/43162) 
  - 다른 팀원이 시도한 방식을 듣고 혜선님이 [유니온 파인드 알고리즘](https://ip99202.github.io/posts/%EC%9C%A0%EB%8B%88%EC%98%A8-%ED%8C%8C%EC%9D%B8%EB%93%9C(Union-Find)/)을 떠올렸음

### 1017

- 카테고리: [최단경로](https://www.acmicpc.net/step/26)
  - 혜선님의 최단경로 풀이법: dfs, bfs 처럼 코드에 틀이 있어서, 다익스트라를 공부하면 문제를 풀 수 있습니다!    ~~노스트라다무스~~
- 랜덤문제: [이분탐색](https://school.programmers.co.kr/learn/courses/30/parts/12486)의 [입국심사](https://school.programmers.co.kr/learn/courses/30/lessons/43238)
  - 주어진 시간 동안 모든 심사관은 총 몇 명을 심사할 수 있는가를 확인하면서 시간 범위를 줄여나가는 것이 포인트. 
  
### 1024

- 카테고리: [투포인터](https://www.acmicpc.net/step/59) + [최단경로](https://www.acmicpc.net/step/26)
  - 투포인터의 [냅색문제](https://www.acmicpc.net/problem/1450)에서 비트 시프트 연산자 ([왼쪽 시프트](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Left_shift), [오른쪽 시프트](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Right_shift))
  - 한 범위가 2개로 나뉘어 져서 각각의 부분합을 구함
- 랜덤문제: [그래프](https://school.programmers.co.kr/learn/courses/30/parts/14393)의 [방의개수](https://school.programmers.co.kr/learn/courses/30/lessons/49190)
  - 레벨5의 고난이도 문제 
    - ![Screen Shot 2022-10-24 at 9 39 43 PM](https://user-images.githubusercontent.com/40953167/197527473-70fca604-768d-4cb9-87a1-30d8d90cbcfa.png)
~~풀었으면 반4자2를 얻을 수 있었던 문제..~~
  - 모래시계 같은 도형도 확인하기 위해서 ```dx,dy = [0,1,1,1,0,-1,-1,-1],[1,1,0,-1,-1,-1,0,1]```를 두번씩 더한다. 1x1를 2x2라고 생각하면 된다.

### 1031

- 카테고리: [동적 계획법과 최단거리 역추적](https://www.acmicpc.net/step/41)
  - 취업준비로 인해 문제를 많이 풀어오지 않아서 앞으로 진행방식을 변경함. 
    > 각자 맡은 문제를 설명하고 다른 방식으로 푼 팀원이 첨언하기.
  - 다음 주에 설명할 문제
    - LCS 2 ➡️ 혜선 / 숨바꼭질 4 ➡️ 유진 / DSLR ➡️ 하영 / 최소비용 구하기 2 ➡️ 혜진 / 플로이드 2 ➡️ 보선
- 랜덤문제: [해시](https://school.programmers.co.kr/learn/courses/30/parts/12077)의 [위장](https://school.programmers.co.kr/learn/courses/30/lessons/42578)
  - 대부분 수학의 조합 방식으로 풀었다
  - 보선님이 알려준 꿀팁: Javascript의 Map을 iterable하게 접근하는 방법은 [for ... of](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of)를 사용하는 것이다.
  - 혜선님이 알려준 꿀팁: 기본값을 생성해주는 딕셔너리 자료형 ```from collections import defaultdict```
    - 관련 글 갈무리 ([출처: daleseo.com](https://www.daleseo.com/python-collections-defaultdict/#%EB%8D%94-%EB%82%98%EC%9D%80-%EB%B0%A9%EB%B2%95-collectionsdefaultdict))
      > 파이썬의 내장 모듈인 collections의 defaultdict 클래스는 이러한 경우 사용하면 딱 인데요. defaultdict 클래스의 생성자로 기본값을 생성해주는 함수를 넘기면, 모든 키에 대해서 값이 없는 경우 자동으로 생성자의 인자로 넘어온 함수를 호출하여 그 결과값으로 설정해줍니다. 

### 1107

- 카테고리: [동적 계획법과 최단거리 역추적](https://www.acmicpc.net/step/41)
  - LCS2
    - 2차원 배열에서 문자가 같으면 이전 값과 1을 더해서 저장한다. (가장자리에도 같은 방식으로 값을 넣기 위해서 패딩 값을 넣어준다.)
    - 2차원 배열을 이용해서 역추적을 하여 부분 문자열을 출력한다. 
    - [LCS 참고 블로그](
https://velog.io/@emplam27/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B7%B8%EB%A6%BC%EC%9C%BC%EB%A1%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94-LCS-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Longest-Common-Substring%EC%99%80-Longest-Common-Subsequence)
  - 숨바꼭질4
    - bfs로 -1, 1, *2 인 상황을 모두 접근한다 (위치값을 같이 저장한다)
  - DSLR
    - 프로그래머스 조이스틱과 유사한 문제
    - 방문 사실을 저장하면서 전체를 다 훑어본다.
  - 최소비용 구하기 2
    - [다익스트라](https://m.blog.naver.com/ndb796/221234424646) 이용
      - 힙을 사용하면 시간복잡도가 작아진다.
  - 플로이드 2
    - 플로이드 워셜 알고리즘 이용 ([알고리즘 참고 블로그](https://m.blog.naver.com/PostView.naver?blogId=ndb796&logNo=221234427842))
    - [문제 설명 때 참고한 그림](https://velog.io/@diddnjs02/%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8%EB%B0%B1%EC%A4%80-%ED%94%8C%EB%A1%9C%EC%9D%B4%EB%93%9C11404%EB%B2%88)
    
### 1114

- 카테고리: [트리](https://www.acmicpc.net/step/23)
  - 트리의 부모 찾기(11725)
  - 트리의 지름(1967)
    - 첫 노드에서 가장 멀리 떨어져있는 노드를 찾고, 그 노드에서 가장 멀리 떨어져 있는 노드의 거리를 찾으면 그게 트리의 지름이다.
    - 증명이 어려워서 완벽히 이해하지 못했다.
  - 트리 순회(1991)
    - 재귀를 이용하여 전위순회, 중위순회, 후위순회
  - 트리의 순회(2263)
    - 후위순회의 마지막이 항상 루트 노드이고, 중위순회는 루트노드를 중심으로 왼쪽자식트리와 오른쪽자식트리를 구분지을 수 있다. 이때, 자식트리들의 개수를 알아내서 후위순회에서도 왼쪽자식트리의 범위를 구하고 오른쪽자식트리의 범위를 구한다. 각 자식트리의 루트를 구해서 중위순회에서 자식의 자식트리를 구한다. (반복)
  - 이진 검색 트리(5639)
    - 부모노드를 기점으로 왼쪽자식은 부모노드보다 작고, 오른쪽자식은 부모노드보다 크다는 특징을 유념하고 전위순회로 트리를 파악하여 후위순회 결과를 구한다.
  - 트리(4803)
    - 그래프의 모든 노드를 확인하여 트리가 만들어지는지(사이클이 없는지) 확인한다.
- 랜덤문제: [스택/큐](https://school.programmers.co.kr/learn/courses/30/parts/12081)의 [기능개발](https://school.programmers.co.kr/learn/courses/30/lessons/42586)
  - 주먹구구 방식 대신에, 첫번째 프로그래스가 완료되려면 며칠이 지나야하는지 계산하면 더 빠르다.
  - 모든 프로그레스가 필요한 날짜를 계산하여 처리하는 방법도 있다.

### 계획 변경

- 코테에 자주 나오는 문제를 집중적으로 풀기 위해서 문제집 변경
  - [바킹독 공개문제집](https://www.acmicpc.net/workbook/by/BaaaaaaaaaaarkingDog)

### 1121

- 카테고리: [BFS](https://www.acmicpc.net/workbook/view/7313)
- 랜덤문제: [힙](https://school.programmers.co.kr/learn/courses/30/parts/12117)
