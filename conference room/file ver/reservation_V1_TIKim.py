from datetime import *
from time import *
Lets = []
with open('Lets.csv', 'r') as f:
        lines = f.readlines()
        for line in lines[1:]:
                line = line.strip()
                Lets.append(line.split(","))

Rolling = []
with open('Rolling.csv', 'r') as f:
        lines = f.readlines()
        for line in lines[1:]:
                line = line.strip()
                Rolling.append(line.split(","))

Double = []
with open('Double.csv', 'r') as f:
        lines = f.readlines()
        for line in lines[1:]:
                line = line.strip()
                Double.append(line.split(","))

def new_room_file():
    with open('Lets.csv', 'w') as f:
        f.write('년도,월,일,시간,이름,인원,비밀번호\n')
    with open('Rolling.csv', 'w') as f:
        f.write('년도,월,일,,시간,이름,인원,비밀번호\n')
    with open('Double.csv', 'w') as f:
        f.write('년도,월,일,,시간,이름,인원,비밀번호\n')

def make_date_Room_name(Room_name):
        year = int(input('확인하실 년도를 숫자로 입력해 주세요. : '))
        month = int(input('확인하실 달을 숫자로 입력해 주세요. : '))
        if month == 12:
                make_day = datetime(year+1, 1, 1) 
        else:
                make_day = datetime(year, month+1, 1)
        make_day_2 = datetime(year, month, 1)
        diff = make_day - make_day_2
        dat_e = int(diff.days)
        for day in range(1, dat_e+1):
                da_te = datetime(year, month, day)
                if da_te.strftime('%w') == '1':
                        day_week = '월'
                        ye_ar = int(da_te.strftime('%Y'))
                        mon_th = int(da_te.strftime('%m'))
                        da_y = int(da_te.strftime('%d'))
                        same_day = []
                        for i in range(len(Room_name)):
                                if ye_ar == int(Room_name[i][0]) and mon_th == int(Room_name[i][1]) and da_y == int(Room_name[i][2]):
                                        same_day.append('a')
                                else:
                                        continue
                        reservation = len(same_day)
                        print(f'{ye_ar} - {mon_th} - {da_y}({day_week}) : 예약 {reservation} 건')

                                
                elif da_te.strftime('%w') == '2':
                        day_week = '화'
                        ye_ar = int(da_te.strftime('%Y'))
                        mon_th = int(da_te.strftime('%m'))
                        da_y = int(da_te.strftime('%d'))
                        same_day = []
                        for i in range(len(Room_name)):
                                if ye_ar == int(Room_name[i][0]) and mon_th == int(Room_name[i][1]) and da_y == int(Room_name[i][2]):
                                        same_day.append('a')
                                else:
                                        continue
                        reservation = len(same_day)
                        print(f'{ye_ar} - {mon_th} - {da_y}({day_week}) : 예약 {reservation} 건')
                        
                elif da_te.strftime('%w') == '3':
                        day_week = '수'
                        ye_ar = int(da_te.strftime('%Y'))
                        mon_th = int(da_te.strftime('%m'))
                        da_y = int(da_te.strftime('%d'))
                        same_day = []
                        for i in range(len(Room_name)):
                                if ye_ar == int(Room_name[i][0]) and mon_th == int(Room_name[i][1]) and da_y == int(Room_name[i][2]):
                                        same_day.append('a')
                                else:
                                        continue
                        reservation = len(same_day)
                        print(f'{ye_ar} - {mon_th} - {da_y}({day_week}) : 예약 {reservation} 건')
                        
                elif da_te.strftime('%w') == '4':
                        day_week = '목'
                        ye_ar = int(da_te.strftime('%Y'))
                        mon_th = int(da_te.strftime('%m'))
                        da_y = int(da_te.strftime('%d'))
                        same_day = []
                        for i in range(len(Room_name)):
                                if ye_ar == int(Room_name[i][0]) and mon_th == int(Room_name[i][1]) and da_y == int(Room_name[i][2]):
                                        same_day.append('a')
                                else:
                                        continue
                        reservation = len(same_day)
                        print(f'{ye_ar} - {mon_th} - {da_y}({day_week}) : 예약 {reservation} 건')
                        
                elif da_te.strftime('%w') == '5':
                        day_week = '금'
                        ye_ar = int(da_te.strftime('%Y'))
                        mon_th = int(da_te.strftime('%m'))
                        da_y = int(da_te.strftime('%d'))
                        same_day = []
                        for i in range(len(Room_name)):
                                if ye_ar == int(Room_name[i][0]) and mon_th == int(Room_name[i][1]) and da_y == int(Room_name[i][2]):
                                        same_day.append('a')
                                else:
                                        continue
                        reservation = len(same_day)
                        print(f'{ye_ar} - {mon_th} - {da_y}({day_week}) : 예약 {reservation} 건')

                else:
                        continue
                
def make_time(Room_name, choice_year, choice_month, choice_day):
        print(f'{choice_year}년 {choice_month}월 {choice_day}일의 예약 가능 시간입니다.')
        able_time = []
        able_time_2 = []
        for j in range(8,17):
                for i in range(len(Room_name)):
                        if j == 12:
                                continue
                        elif j == int(Room_name[i][3]):
                                if int(choice_year) == int(Room_name[i][0]) and int(choice_month) == int(Room_name[i][1]) and int(choice_day) == int(Room_name[i][2]):
                                        continue
                                else:
                                        able_time.append(j)     
                        else:
                                able_time.append(j)
        for i in range(8,17):
                if able_time.count(i) == len(Room_name):
                        able_time_2.append(i)
                else:
                        continue
        for i in able_time_2:
               print(f'{i}시')

def room_choice():
    room = int(input('1. Lets\n2. Rolling\n3. Double\n예약하실 회의실의 번호를 입력해주세요. (ex : 1) : '))
    if room == 1:
        with open('Lets.csv', 'a') as f:
            make_date_Room_name(Lets)
            choice_year = int(input('원하는 날짜의 년도를 입력해 주세요. (ex : 2000) : '))
            choice_month = int(input('원하는 날짜의 월을 입력해 주세요. (ex : 5) : '))
            choice_day = int(input('원하는 날짜의 일자를 입력해 주세요. (ex : 1) : '))
            make_time(Lets, choice_year, choice_month, choice_day)
            time = int(input('원하는 시간을 선택해 주세요. (ex : 14) : '))
            name = input('예약자분의 성함을 입력해 주세요. : ')
            number_of_people = int(input('이용하실 분들의 총 인원수를 숫자로 입력해 주세요. (ex : 5) : '))
            password = str(input('비밀번호 4자리를 설정해주세요. (ex : 2012) : '))
            f.write(f'{choice_year},{choice_month},{choice_day},{time},{name},{number_of_people},{str(password)}\n')

    elif room == 2:
        with open('Lets.csv', 'a') as f:
            make_date_Room_name(Rolling)
            choice_year = int(input('원하는 날짜의 년도를 입력해 주세요. (ex : 2000) : '))
            choice_month = int(input('원하는 날짜의 월을 입력해 주세요. (ex : 5) : '))
            choice_day = int(input('원하는 날짜의 일자를 입력해 주세요. (ex : 1) : '))
            make_time(Lets, choice_year, choice_month, choice_day)
            time = int(input('원하는 시간을 선택해 주세요. (ex : 14) : '))
            name = input('예약자분의 성함을 입력해 주세요. : ')
            number_of_people = int(input('이용하실 분들의 총 인원수를 숫자로 입력해 주세요. (ex : 5) : '))
            password = str(input('비밀번호 4자리를 설정해주세요. (ex : 2012) : '))
            f.write(f'{choice_year},{choice_month},{choice_day},{time},{name},{number_of_people},{str(password)}\n')
    
    elif room == 3:
        with open('Lets.csv', 'a') as f:
            make_date_Room_name(Double)
            choice_year = int(input('원하는 날짜의 년도를 입력해 주세요. (ex : 2000) : '))
            choice_month = int(input('원하는 날짜의 월을 입력해 주세요. (ex : 5) : '))
            choice_day = int(input('원하는 날짜의 일자를 입력해 주세요. (ex : 1) : '))
            make_time(Lets, choice_year, choice_month, choice_day)
            time = int(input('원하는 시간을 선택해 주세요. (ex : 14) : '))
            name = input('예약자분의 성함을 입력해 주세요. : ')
            number_of_people = int(input('이용하실 분들의 총 인원수를 숫자로 입력해 주세요. (ex : 5) : '))
            password = str(input('비밀번호 4자리를 설정해주세요. (ex : 2012) : '))
            f.write(f'{choice_year},{choice_month},{choice_day},{time},{name},{number_of_people},{str(password)}\n')
    
    else: 
        print('등록되지 않은 방 번호 입니다.')

num = 0

while num !=3:
        num = int(input('1. 파일 생성 및 초기화\n2. 예약 내역 조회 및 예약\n3. 끝내기\n 원하는 번호를 입력해 주세요 . : '))
        if num == 1:
                new_room_file()
                continue
        elif num == 2:
                room_choice()
                continue
        elif num == 3:
                break