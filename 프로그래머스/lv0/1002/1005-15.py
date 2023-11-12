# 겹치는 선분의 길이
def solution(lines):
    def create_set(start, end):
        return set(range(start, end))

    s1 = create_set(lines[0][0], lines[0][1])
    s2 = create_set(lines[1][0], lines[1][1])
    s3 = create_set(lines[2][0], lines[2][1])

    common_intersection = (s1 & s2) | (s2 & s3) | (s1 & s3)
    return len(common_intersection)
