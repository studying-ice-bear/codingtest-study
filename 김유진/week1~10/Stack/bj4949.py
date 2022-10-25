import sys
strings = ""
sentence = ""

while True:
    stack = []
    answer = "yes"
    sentence = sys.stdin.readline()

    if sentence == ".\n":
        break

    for i in range(len(sentence)):
        if sentence == ".":
            break
        if sentence[i] == "(" or sentence[i] == "[":
            stack.append(sentence[i])
        elif sentence[i] == ")" and stack:
            if stack[-1] == "(":
                stack.pop()
            else:
                answer = "no"
                break
        elif sentence[i] == ")" and not stack:
            answer = "no"
            break
        elif sentence[i] == "]" and stack:
            if stack[-1] == "[":
                stack.pop()
            else:
                answer = "no"
                break
        elif sentence[i] == "]" and not stack:
            answer = "no"
            break

    if stack:
        answer = "no"

    print(answer)