# 영어가 싫어요
def solution(numbers):
    answer = ''
    arr = ["zero", "one", "two", "three", "four",
           "five", "six", "seven", "eight", "nine"]
    if x in arr:
        n = arr.index(x)
        answer += n

    return answer


if __name__ == "__main__":
    numbers = "onetwothreefourfivesixseveneightnine"
    # print(solution)

    answer = ''

    arr = ["zero", "one", "two", "three", "four",
           "five", "six", "seven", "eight", "nine"]

    if numbers in arr:
        n = arr.index(numbers)
        answer += n

    print(answer)
