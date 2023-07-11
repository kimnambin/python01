# 함수
def operator(a, b):
    add_var = a + b
    subtract_var = a - b
    multiply_var = a * b
    divide_var = a / b
    return add_var, subtract_var, multiply_var, divide_var

a, b, c, d = operator(7, 3)
print('4칙 연산 함수를 호출합니다:')
print(a, b, c, d)

def gugudan(num):
    for i in range(1, 10):
        print(f'구구단을 출력합니다: {num} x {i} = {num * i}')

gugudan(3)
