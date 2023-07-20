n = int(input('수열값 n을 입력하세요: '))
A = list(map(int, input('수열 A를 입력하세요: ').split()))
m = int(input('합 M을 입력하세요: '))

count = 0
interval_sum = 0
end = 1

# start를 차례대로 증가시키며 반복
for start in range(n):
    # end를 가능한 만큼 이동시키기
    while interval_sum < m and end < n:
        interval_sum += A[end]
        end += 1

    # 부분합이 m일 때 카운트 증가
    if interval_sum == m:
        count += 1
    interval_sum -= A[start]

print(count)

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
print("수행 시간:", end_time - start_time , '초')  

# 교수님 정답

n, m = map(int, input("개수 , 합 입력: ").split())
data = list(map(int, input('데이터 직접 입력: ').split()))

count = 0
interval_sum = 0
end = 0

for start in range(n):
    print("시작: ", start)
    # end를 가능한 만큼 이동시키기
    while interval_sum < m and end < n:
        interval_sum += data[end]
        print("끝: ", end)
        end += 1

    # 부분합이 m일 때 카운트 증가
    if interval_sum == m:
        print("중간 카운트: ", count)
        count += 1
            
    interval_sum -= data[start]

print("카운트: ", count)

            
