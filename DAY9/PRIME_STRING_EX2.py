import math

# 소수인지를 판별하는 함수
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# 가장 큰 소수를 찾는 함수
def find_largest_prime(string):
    n = len(string)
    max_prime = -1

    # 모든 부분 문자열을 추출하여 소수인지 확인
    for i in range(n):
        for j in range(i + 1, n + 1):
            sub_str = string[i:j]
            num = int(sub_str)
            if is_prime(num):
                max_prime = max(max_prime, num)

    return max_prime

if __name__ == "__main__":
    num_string = input("숫자로 이루어진 문자열을 입력하세요: ")
    result = find_largest_prime(num_string)
    if result == -1:
        print("소수가 없습니다.")
    else:
        print("가장 큰 소수:", result)

