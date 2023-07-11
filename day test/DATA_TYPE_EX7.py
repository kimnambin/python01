# 문제 : 리스트에 문자열을 저장하고 출력	
# 리스트 [] 선언, append 함수(내용 추가) 활용
# While문 내에서 입력 받기 : if 엔터( ‘ ‘ ) 누르면 정지
# 리스트 컴프리핸션 전체 출력 : for문

# 내가 풀어본 정답
array = []

while True:
    c = input("문자를 입력하세요: ")
    if c == '':
        break
    print(c)
    array.append(c)

for c in range(0, ):
    array.append(c)

print(array)

# 교수님 정답
input_lst = []
while True:
    name = input('저장할 이름을 입력 :')
    if name == '':
        break
        input_lst.append(name)
        
        print('입력한 이름의 전체 목록 :')
        for name in input_lst:
            print(name , end= ',')