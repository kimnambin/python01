# H 입력 받기
h = int(input('1시~23시 사이 시간 입력 : '))
count = 0
for i in range(h + 1): # 시간 
    for j in range(60): # 분
        for k in range(60): # 초
            if '3' in str(i) + str(j) + str(k): # 매 시각 안에 '3'이 하나라도 포함되어 있다면 참
                count += 1 # 카운트 증가
        print(count)
print('최종 3이 카운트 된 결과는 :', count)

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


# 다 1초가 넘지 않음