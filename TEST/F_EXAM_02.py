
K, N = map(int, input("가래떡의 개수(K)와 만들 떡볶이 떡의 개수(N)을 입력하세요(공백으로 구분) : ").split())
array = list(map(int, input('각 가래떡의 길이를 입력하세요(공백으로 구분) :').split()))

start, end = 0, max(array)

result = 0
while start <= end:
    mid = (start + end) // 2
    count = sum([(x // mid) for x in array])
    if count >= N:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)


