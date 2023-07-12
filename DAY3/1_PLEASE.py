n, k = map(int, input('두 수를 공백으로 분리하여 입력 : ').split()) # N, K을 공백을 기준으로 구분하여 입력 받기
result = 0
while True: # 반복 루프 시작
    target = (n // k) * k # K로 나누어 지는 수를 구함, 예) 25 나누기 4 곱하기 4 = 처음 24
    result += (n - target) # N이 K로 나누어 떨어지는 수가 될 때까지 빼기, 1
    n = target # 25를 24로 수정 
    if n < k: # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
        break
    result += 1 # 횟수 증가
    n //= k # K로 나누기, n = 6
result += (n - 1) # 마지막으로 남은 수에 대하여 1씩 빼기, 6, 5 --> 4일때까지 2번 추가 빼기, 마지막 1번 나누고

print('1이 도달하기 까지 연산 횟수 :', result) # 총 5번 횟수 연산

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
end_time = time.time() # 측정 종료
print("time:", end_time - start_time) # 수행 시간 출력