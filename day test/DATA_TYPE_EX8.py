# 문제 : 튜플에 리스트 문자열을 저장하고 출력
# 튜플 () 선언
# 기존 리스트 데이터 받아 튜플로 캐스팅 후 출력

tuple_a = ()
input_lst = []

while True:
    name = input('저장할 이름을 입력하세요: ')
    if name == '':
        break
    input_lst.append(name)

print('입력한 이름의 전체 목록:')
for name in input_lst:
    print(name, end=', ')

print('\n튜플로 캐스팅 후 출력:')
tuple_a = tuple(input_lst)
print(tuple_a)

