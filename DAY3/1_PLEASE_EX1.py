# 문제 : 1일 될때까지 예제의 시간복잡도, 공간 복잡도를 분석한다.
# 문제 예제에서 요구하는 기준에 적합한가? 시간 2초, 메모리 128MB
# 참고 : N = 25, K = 4로 값 미리 정의

n = 25
k = 4

result = 0
while True:
    target = (n // k) * k
    result += (n - target)
    n = target
    if n < k:
        break
    result += 1
    n //= k
result += (n - 1)

print('1이 도달하기 까지 연산 횟수:', result)

import time
import random

start_time = time.time()  # 측정 시작
array = []  # 리스트 생성

for _ in range(2000):  # 변수 v를 사용하지 않으므로 _로 대체
    array.append(random.randint(0, 10))  # 랜덤 값 추가

temp = 0  # 변수 temp를 반복문 밖에서 초기화

for i in array:
    for j in array:
        temp = i * j
        # print(temp) - 반복마다 값 출력?

print("측정 최종 값 출력:", temp , 'MB')
end_time = time.time()  # 측정 종료
print("수행 시간:", end_time - start_time , '초')  # 수행 시간 출력
