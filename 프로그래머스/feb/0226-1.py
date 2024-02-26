# 모의고사

def solution(answers):
    answer = []
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    scores = [0, 0, 0]

    for i, ans in enumerate(answers):
        for j, pattern in enumerate(patterns):
            if ans == pattern[i % len(pattern)]:
                scores[j] += 1

    max_score = max(scores)

    for i, score in enumerate(scores):
        if score == max_score:
            answer.append(i + 1)

    return answer
