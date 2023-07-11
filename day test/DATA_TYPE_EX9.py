# 문제 : 국어, 수학, 영어, 도덕, 물리 5개 과목의 데이터를 dic_sum 사전으로 생성하고, 전체 평균 점수를 구하시오.
# 점수는 직접 입력한다. (전체 점수 / 과목 개수)

# 내가 풀어본 정답
dic_sum = dict()
dic_sum['국어'] = 70
dic_sum['수학'] = 60
dic_sum['영어'] = 100
dic_sum['도덕'] = 100
dic_sum['물리'] = 0

print(dic_sum , '전체 평균 점수는 :')
print(sum(dic_sum.values()) / len(dic_sum))

# 교수님 정답
dic_sum = {'국어':70 , '수학' : 60 , '영어': 100 , '도덕' : 100 , '물리' : 0}
averge = sum(dic_sum.values()) / len(dic_sum) # 전체 점수 / 과목 개수
print('사전 자료구조를 활용 , 전체 평균 점수는 :')
print(averge)


