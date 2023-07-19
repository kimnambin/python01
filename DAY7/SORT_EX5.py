# 챗지피티 정답 (bisect 라이브러리 사용)

import bisect

# 매장 내의 부품 개수(N) 입력
n = int(input("매장 내의 부품 개수(N)를 입력하세요: "))

# 매장 내의 부품 목록 입력
print("매장 내의 부품 번호를 입력하세요 (공백으로 구분):")
parts_in_store = list(map(int, input().split()))

# 대량으로 납품해야 하는 부품 종류 개수(M)와 대량으로 납품해야 하는 부품 종류 입력
m = int(input("대량으로 납품해야 하는 부품 종류 개수(M)를 입력하세요: "))
print("대량으로 납품해야 하는 부품 종류를 입력하세요 (공백으로 구분):")
delivery_parts = list(map(int, input().split()))

# 이진 탐색을 통해 부품의 존재 여부를 확인하는 함수
def check_parts(part_list, delivery_list):
    part_list.sort()

    for part in delivery_list:
        index = bisect.bisect_left(part_list, part)
        if index < len(part_list) and part_list[index] == part:
            print("Yes")
        else:
            print("No")

check_parts(parts_in_store, delivery_parts)


# 교수님 정답 
import sys
import bisect

si = sys.stdin.readline
n = int(si())
store = sorted(map(int, si().split()))
m = int(si())
wish = list(map(int, si().split()))

for x in wish:
    idx = bisect.bisect_left(store, x)
    
    if idx < len(store) and store[idx] == x:  # 인덱스 범위를 확인하여 IndexError를 방지합니다.
        print('yes', end='')
    else:
        print('no', end='')
