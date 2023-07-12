# 문제 : N종류의 동전을 사용할 수 있다. 가격의 합 K를 만드는 동전 개수의 최소값을 출력하시오.
# 참고 : 첫 째 줄에 N과, K가 주어진다.
# 범위 : (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)
# 참고 : 둘째 줄부터 동전의 가치 Ai가 오름차순으로 주어진다.
# 범위 : (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수) 큰동전은 작은 동전의 배수라는 의미
# 요구사항 : 시간 제한 1초, 메모리 제한 256MB


N = 10
K = 4200

count = 0

coins = [1, 5, 50, 100, 500, 1000, 5000, 10000, 50000]
coins.sort(reverse=True)

for coin in coins:
    count += K // coin
    K %= coin

print('동전의 최소 개수는:', count, '개')

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



# 챗 지피티의 다른 방법 (동적 계획법?)
N = 10
K = 4200

INF = int(1e9)  # 무한을 의미하는 값으로 초기화
dp = [INF] * (K + 1)  # 동전 개수의 최소값을 저장할 DP 테이블

coins = [1, 5, 50, 100, 500, 1000, 5000, 10000, 50000]

dp[0] = 0  # 0원을 만들기 위한 동전 개수는 0개

for coin in coins:
    for i in range(coin, K + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)

print('동전의 최소 개수는:', dp[K], '개')

# 교수님 정답 (입력으로 하셨음)
N , K = map(int , input('화폐 개수와 돈의 가격 입력 : ').split())
coins = [] 

for _ in range(N):
    coins.append(int(input('동전 가격을 개수만큼 입력 : ')))
    coins.sort(reverse=True)
    
    count_currency = 0
    for coin in coins:
        if K >= coin:
            count_currency += K
            K %= coin
            if K <= 0:
                break
                
                print('거슬러 준 동전의 개수 : ' , count_currency)