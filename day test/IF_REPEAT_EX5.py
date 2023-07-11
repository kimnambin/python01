# 조건문 , 반복문 도전 5
i = int(input('입력받은 x부터 9단까지 구구단 출력: '))
for x in range(i, 10):
    for j in range(1, 10):
        print(x, "X", j, "=", x * j)
    print()  # 한 단 출력 후 줄 바꿈