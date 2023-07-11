# 문제 : ‘abcdefg123123123aaa’ a 문자를 ‘A’로 변경하기
# 문자열 타입 변수 선언 및 초기화, replace 함수 활용하기

# 내가 풀어본 부분
s = "abcdefg123123123aaa"
print(s.find("a"))
print(s.replace('a', 'A'))

# 교수님 정답
str = "abcdefg123123123aaa"
str_result = str.replace("a", "A")
print(str_result)
