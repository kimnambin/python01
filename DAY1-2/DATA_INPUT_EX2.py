#입력과 출력 도전 2
s = input('주민등록번호를 입력해주세요: ').split('-')
print(s)
print(''.join(s))

print(''.join(input('주민등록번호를 입력해주세요, -으로 구분: ').split('-')))
