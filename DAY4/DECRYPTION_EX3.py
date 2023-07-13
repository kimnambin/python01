# 문제 : 홍길동은 비밀 문서를 가지고 다닌다. 소문자 모음(‘a’, ‘e’, ‘I’, ‘o’, ‘u’)의 다음에 ‘g’를 한 개 쓰고, 그 모음을 하나 더 쓰는 형태로 문서를 암호화한다. 암호문을 실제 원본 문장으로 바꾸는 프로그램을 작성하시오.
# 참고 : 내용은 알파벳 소문자와 공백으로 이루어진 문장 한개
# 참고 : 길이는 최대 100

word = input("모음 뒤에는 g를 넣어서 단어를 입력해주세요: ")
output = ''
group = ('a', 'e', 'i', 'o', 'u')

skip_next = False  # 모음 'g' 다음 글자를 건너뛰기 

for i in range(len(word)):
    if skip_next:
        skip_next = False
        continue

    if word[i] == 'g' and i + 1 < len(word) and word[i+1] in group :
        skip_next = True
        continue

    output += word[i]

print(output)


