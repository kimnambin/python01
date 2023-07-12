# 문제 : 여러 개의 카드 중에서 가장 높은 숫자가 쓰인 카드를 뽑자. N X M 형태로 나열되어 있다. N은 행의 개수, M은 열의 개수이다. 
# 참고 : 행을 순차 선택, 첫 뽑기는 반드시 가장 낮은 카드를 한번 이상 뽑아야한다. 
# 범위 : 행열 : (1 <= N, N <= 100),  카드  숫자 : 자연수 10000 이하 
# 요구사항 : 시간 제한 1초, 메모리 제한 128MB

N, M = map(int, input('N은 행의 개수, M은 열의 개수: ').split())

max_card = 0  # 가장 높은 숫자가 쓰인 카드
for _ in range(N):
    cards = list(map(int, input('카드 숫자 입력 (숫자는 자연수 10000 이하): ').split()))
    min_card = min(cards)  # 행마다 가장 낮은 카드 선택
    max_card = max(max_card, min_card)  # 현재까지의 가장 높은 숫자와 비교하여 갱신

print('가장 높은 숫자가 쓰인 카드:', max_card)

