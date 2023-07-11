# 문제 : 입력으로 들어오는 모든 수의 평균값 계산하는 함수 작성하기
# 입력 개수는 가변이다. 함수 이름 : avg
# 리스트 활용, for문, append로 데이터 저장
# 전체 합  / len 함수 = 평균을 리턴


# 내 정답
input_list = []

while True:
    num = input('숫자를 입력하세요: ')
    if num == '':
        break
    input_list.append(int(num))

print('입력한 숫자의 전체 목록:')
for num in input_list:
    print(num, end=', ')
    
def add(nums):
    num_sum = sum(nums)
    print('숫자를 모두 더합니다:', num_sum)
    return num_sum

total_sum = add(input_list)
avg = total_sum / len(input_list)
print('전체 평균은:')
print(avg)


# 교수님 정답
def avg(*avg):
    arr = [] # 리스트 변수 선언
    for i in args:
        arr.append(i) # 매개변수를 각각 추가 저장
        
        temp = 0
        for j in arr:
            temp += j # temp에 합한 결과를 누저ㅗㄱ
            
            return temp / len(arr) # 평균 계산 리턴
        
        print('입력된 정수의 평균을 출력 :' , avg(1,2,2,2,2,3,3,3,4,5))