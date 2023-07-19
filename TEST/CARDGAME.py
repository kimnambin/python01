# 문제 : 특정 숫자에서 X개를 제거하여 가장 큰 숫자 출력하는 프로그램을 완성하라. 예) 1231에서 두 수를 제거하면 12, 13, 11, 21, 23, 31을 만들 수 있다. 이중 가장 큰 숫자는 31이다. 
# 참고 : 입력 - 문자열 숫자 S, 제거 숫자 개수 X
# 참고 : S는 2자리 이상 정수, X는 1이상 자연수


s = input('2자리 이상 정수s를 입력해 주세요: ')
x = int(input('제거할 1 이상 자연수x를 입력해 주세요: '))

digits = [int(digit) for digit in s]  # 정수를 각 자리수로 분리하여 리스트에 저장
digits.sort(reverse=True)  # 자릿수를 내림차순으로 정렬

if x >= len(digits):
    max_number = 0  # 제거할 수 있는 자리수보다 x가 크거나 같은 경우, 모든 자리수를 제거하여 0을 출력
else:
    max_number = int(''.join(map(str, digits[:-x])))  # 가장 작은 x개의 자리수를 제거한 후, 남은 자리수를 합쳐서 정수로 변환

print(max_number)

