# 문제 : A, B, C가 주어졌을때 W(A, B, C)를 출력하는 프로그램을 작성하시오. 
# 참고 : 입력은 3개 정수, 한줄에 하나씩 입력된다. 범위 : -50 ≤ a, b, c ≤ 50
# 참고 :  입력의 마지막은 -1 -1 -1로 나타내며, 3개 정수가 모두 -1인 경우 입력의 마지막을 제외하면 없다. 

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1  # 부피는 0 이상이어야 함

    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)  # 최대 크기 20

    if a < b and b < c:
        return w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

    else:
        return w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    else:
        print(w(a, b, c))


