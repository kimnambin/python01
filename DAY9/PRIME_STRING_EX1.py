# 에라토스테네스의 체 적용
import math

n = 100000 # 2부터 1,000까지의 모든 수에 대하여 소수 판별
# 처음엔 모든 수가 소수(True)인 것으로 초기화(0과 1은 제외)
array = [True for i in range(n + 1)]

# 에라토스테네스의 체 알고리즘 수행
# 2부터 n의 제곱근까지의 모든 수를 확인하며
for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True: # i가 소수인 경우(남은 수인 경우)
        # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

            # 모든 소수 출력
for i in range(2, n + 1):
    if array[i]:
         print(i, end=' ')

        
        
import time
import random

start_time = time.time() # 측정 시작
array = [] # 리스트 생성

for v in range(2000): # N = 500인 경우는?
    array.append(random.randint(0, 10)) # 랜덤 값 추가

for i in array:
    for j in array:
        temp = i *  j
        #print(temp) - 반복마다 값 출력?

print(temp) # 측정 최종 값 출력
end_time = time.time() # 측정 종료
print("time:", end_time - start_time) # 수행 시간 출력