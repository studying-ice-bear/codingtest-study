def concat_dash_and_str(dash, str):
    global answer  # 함수 내에서 전역변수 값을 변경하기 위해서 global 키워드를 사용해서 선언한다.
    answer.append(dash)
    answer.append(str)

def recursion(n, total):
    dash = ""
    if n < total:
        dash = "____" * (total - n)

    concat_dash_and_str(dash, "\"재귀함수가 뭔가요?\"\n")

    if n <= 0:
        concat_dash_and_str(dash, "\"재귀함수는 자기 자신을 호출하는 함수라네\"\n")
    else:
        concat_dash_and_str(dash, "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.\n")
        concat_dash_and_str(dash, "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.\n")
        concat_dash_and_str(dash, "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"\n")
        recursion(n - 1, total)

    concat_dash_and_str(dash, "라고 답변하였지.\n")


n = int(input())
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
answer = []
# python에서 string은 immutable한 자료형이기 때문에 수정한 만큼 gc를 실행하게 된다.
# 실행 속도를 높이기 위해서 list의 append 함수를 이용해서 String Builder 역할을 하게 한다.
# 출처: https://www.pymoon.com/entry/파이썬에서-문자열-합치기 [파이문:티스토리]
recursion(n, n)
print(''.join(answer))
# str.join(iterable) 함수
# document: https://docs.python.org/3/library/stdtypes.html#str.join
# 이터러블에 담긴 문자열을 합치는 기능을 함. 문자열이 아니면 TypeError 발생한다.
# str은 문자열들 사이에 넣을 separator 이다.
# 예시: "/".join(["h", "e", "l", "l", "o"]) # h/e/l/l/o
