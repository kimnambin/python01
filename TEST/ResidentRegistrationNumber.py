# s = input('YYYYMMDD-GXXXXXX 양식에 맞게 주민등록번호를 입력해주세요: ').split('-')

# array = [YYYY, MM, DD, G]

# while True:
    # s = input('YYYYMMDD-GXXXXXX 양식에 맞게 주민등록번호를 입력해주세요: ').split('-')
    # if s == '':
       # break
    # print(s)
    # array.append(s)


# for num in array:

    
   # print('생년월일은 년 월 일 입니다' , '성별은 입니다')



rrn = input("주민등록번호를 입력하세요: ")

if len(rrn) != 13 or not rrn.isdigit():
    print("유효하지 않은 주민등록번호입니다.")
else:
    birthdate = f"{rrn[:2]}-{rrn[2:4]}-{rrn[4:6]}"
    century = "19" if int(rrn[6]) < 3 else "20"
    gender = "여성" if int(rrn[6]) % 2 == 0 else "남성"
    print("유효한 주민등록번호입니다.")
    print("생년월일:", century + birthdate)
    print("성별:", gender)

    
    