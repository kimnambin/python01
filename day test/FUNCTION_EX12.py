# 문제 : 1,2,3,4,5가 적힌 숫자 카드가 있다. 세 자리 수를 만들 수 있는 방법은? 서로 다른 숫자 5개 중에서 3개를 택하여 일렬로 출력(순열)

from itertools import permutations
data = ['1', '2', '3', '4', '5'] # 데이터 준비
result = list(permutations(data, 5)) # 모든 순열 구하기
print('모든 순열을 출력 :', result)

from itertools import combinations
data = ['1', '2', '3', '4', '5'] # 데이터 준비
result = list(combinations(data, 3)) # 3개를 뽑는 모든 조합 구하기
print('3개 조합 모두 출력 :', result)

from itertools import product
data = ['1', '2', '3', '4', '5'] # 데이터 준비
result = list(product(data, repeat=3)) # 2개를 뽑는 모든 순열 구하기 (중복 허용)
print('3개 중복 순열 모두 출력 :', result)

from itertools import combinations_with_replacement
data = ['1', '2', '3', '4', '5'] # 데이터 준비
result = list(combinations_with_replacement(data, 3)) # 2개를 뽑는 모든 조합 구하기 (중복 허용)
print('3개 중복 조합 모두 출력 :', result)