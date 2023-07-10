# 문제 1 : 정수(1 ~ 100) 1개를 입력 받아 1부터 그 수까지 짝수의 합을 출력하시오.
# for, while 문 선택

n = int(input("정수를 입력하세요: "))
total = 0
i = 1

while i <= n:
    if i % 2 == 0:
        total += i
    i += 1

print("1부터", n, "까지 짝수의 합:", total)


# 문제 2 : 영문 소문자 q가 입력될 까지 입력 문자를 무한 출력하시오.
# While 문과 if문 활용

while True:
    char = input("문자를 입력하세요: ")
    if char == 'q':
        break
    print(char)

    # n = int(input('1~100사이 정수를 입력하여 짝수만 출력: '))
    # sum=0
    # for i in range
    # 
    #
    #

