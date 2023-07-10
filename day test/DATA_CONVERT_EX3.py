# 문제 정수 3개를 받아 합과 평균 출력하기
#a, b, c = map(int, input('정수 3개를 입력 받아 합을 계산 : ').split())
#print(a + b + c)

#a, b, c = input('정수 3개를 입력 받아 평균을 계산 : ').split()
#d = (int(a) + int(b) + int(c)) // 3

#print('정수 3개의 평균 결과:', d)

a , b , c =input('정수를 3개 입력: ').split()
a= int (a)
b= int (b)
c= int (c)
total = a+b+c
avg = total/3
print(total , format(avg, "2f"))
