# 피보나치 함수(Fibonacci Function)을 재귀함수로 구현
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)

print(fibo(90))
# 단순 재귀 함수 구현  지수 시간 복잡도(10억 이상)
