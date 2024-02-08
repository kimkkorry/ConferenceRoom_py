from datetime import *
from time import *
def new_room_file():
        Room_num = int(input('삭제 및 초기화 할 회의실 파일을 선택해 주세요.\n1. Lets\n2. Rolling\n3. Double\n회의실 번호로 입력해 주세요. (ex : 1) : '))
        if Room_num == 1:
                with open('Lets.csv', 'w') as f:
                        f.write('년도,월,일,시간,이름,인원,비밀번호\n')
                print('Lets 회의실 파일 예약 내역 파일 생성 및 초기화 완료 되었습니다.')
        elif Room_num == 2:
                with open('Rolling.csv', 'w') as f:
                        f.write('년도,월,일,,시간,이름,인원,비밀번호\n')
                print('Rolling 회의실 파일 예약 내역 파일 생성 및 초기화 완료 되었습니다.')
        elif Room_num == 3:        
                with open('Double.csv', 'w') as f:
                        f.write('년도,월,일,,시간,이름,인원,비밀번호\n')
                print('Double 회의실 파일 예약 내역 파일 생성 및 초기화 완료 되었습니다.')
        else:
                print('등록된 방 번호가 아닙니다.')

def make_date_Room_name(Room_name):
        Room_name_str = str(Room_name)
        Room_name_list = []
        with open(f'{Room_name_str}.csv', 'r') as f:
                lines = f.readlines()
                for line in lines[1:]:
                        line = line.strip()
                        Room_name_list.append(line.split(","))
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
                        for i in range(len(Room_name_list)):
                                if ye_ar == int(Room_name_list[i][0]) and mon_th == int(Room_name_list[i][1]) and da_y == int(Room_name_list[i][2]):
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
                        for i in range(len(Room_name_list)):
                                if ye_ar == int(Room_name_list[i][0]) and mon_th == int(Room_name_list[i][1]) and da_y == int(Room_name_list[i][2]):
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
                        for i in range(len(Room_name_list)):
                                if ye_ar == int(Room_name_list[i][0]) and mon_th == int(Room_name_list[i][1]) and da_y == int(Room_name_list[i][2]):
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
                        for i in range(len(Room_name_list)):
                                if ye_ar == int(Room_name_list[i][0]) and mon_th == int(Room_name_list[i][1]) and da_y == int(Room_name_list[i][2]):
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
                        for i in range(len(Room_name_list)):
                                if ye_ar == int(Room_name_list[i][0]) and mon_th == int(Room_name_list[i][1]) and da_y == int(Room_name_list[i][2]):
                                        same_day.append('a')
                                else:
                                        continue
                        reservation = len(same_day)
                        print(f'{ye_ar} - {mon_th} - {da_y}({day_week}) : 예약 {reservation} 건')

                else:
                        continue
                
def make_time(Room_name, choice_year, choice_month, choice_day):
        Room_name_str = str(Room_name)
        Room_name_list = []
        with open(f'{Room_name_str}.csv', 'r') as f:
                lines = f.readlines()
                for line in lines[1:]:
                        line = line.strip()
                        Room_name_list.append(line.split(","))
        print(f'{choice_year}년 {choice_month}월 {choice_day}일의 예약 가능 시간입니다.')
        able_time = []
        able_time_2 = []
        for j in range(8,17):
                for i in range(len(Room_name_list)):
                        if j == 12:
                                continue
                        elif j == int(Room_name_list[i][3]):
                                if int(choice_year) == int(Room_name_list[i][0]) and int(choice_month) == int(Room_name_list[i][1]) and int(choice_day) == int(Room_name_list[i][2]):
                                        continue
                                else:
                                        able_time.append(j)     
                        else:
                                able_time.append(j)
        for i in range(8,17):
                if able_time.count(i) == len(Room_name_list):
                        able_time_2.append(i)
                else:
                        continue
        for i in able_time_2:
               print(f'{i}시')

def room_choice():
    room = int(input('1. Lets\n2. Rolling\n3. Double\n예약하실 회의실의 번호를 입력해주세요. (ex : 1) : '))
    if room == 1:
        Lets_room = []
        with open('Lets.csv', 'r') as f:
                lines = f.readlines()
                for line in lines[1:]:
                        line = line.strip()
                        Lets_room.append(line.split(","))
        with open('Lets.csv', 'a') as f:
            Room_name = 'Lets' 
            make_date_Room_name(Room_name)
            choice_year = int(input('원하는 날짜의 년도를 입력해 주세요. (ex : 2000) : '))
            choice_month = int(input('원하는 날짜의 월을 입력해 주세요. (ex : 5) : '))
            choice_day = int(input('원하는 날짜의 일자를 입력해 주세요. (ex : 1) : '))
            make_time(Room_name, choice_year, choice_month, choice_day)
            time = int(input('원하는 시간을 선택해 주세요. (ex : 14) : '))
            name = input('예약자분의 성함을 입력해 주세요. : ')
            number_of_people = int(input('이용하실 분들의 총 인원수를 숫자로 입력해 주세요. (ex : 5) : '))
            password = str(input('비밀번호 4자리를 설정해주세요. (ex : 2012) : '))
            f.write(f'{choice_year},{choice_month},{choice_day},{time},{name},{number_of_people},{str(password)}\n')
            print(f'{name}님 외 {number_of_people-1}분\n{choice_year}년 {choice_month}월 {choice_day}일 {time}시 ~ {time+1}시 <Lets> 회의실 예약 완료 되었습니다.')

    elif room == 2:
        Rolling_room = []
        with open('Rolling.csv', 'r') as f:
                lines = f.readlines()
                for line in lines[1:]:
                        line = line.strip()
                        Rolling_room.append(line.split(","))
        with open('Rolling.csv', 'a') as f:
            Room_name = 'Rolling'
            make_date_Room_name(Room_name)
            choice_year = int(input('원하는 날짜의 년도를 입력해 주세요. (ex : 2000) : '))
            choice_month = int(input('원하는 날짜의 월을 입력해 주세요. (ex : 5) : '))
            choice_day = int(input('원하는 날짜의 일자를 입력해 주세요. (ex : 1) : '))
            make_time(Room_name, choice_year, choice_month, choice_day)
            time = int(input('원하는 시간을 선택해 주세요. (ex : 14) : '))
            name = input('예약자분의 성함을 입력해 주세요. : ')
            number_of_people = int(input('이용하실 분들의 총 인원수를 숫자로 입력해 주세요. (ex : 5) : '))
            password = str(input('비밀번호 4자리를 설정해주세요. (ex : 2012) : '))
            f.write(f'{choice_year},{choice_month},{choice_day},{time},{name},{number_of_people},{str(password)}\n')
            print(f'{name}님 외 {number_of_people-1}분\n{choice_year}년 {choice_month}월 {choice_day}일 {time}시 ~ {time+1}시 <Rolling> 회의실 예약 완료 되었습니다.')
    
    elif room == 3:
        Double_room = []
        with open('Double.csv', 'r') as f:
                lines = f.readlines()
                for line in lines[1:]:
                        line = line.strip()
                        Double_room.append(line.split(","))
        with open('Double.csv', 'a') as f:
            Room_name = 'Double'
            make_date_Room_name(Room_name)
            choice_year = int(input('원하는 날짜의 년도를 입력해 주세요. (ex : 2000) : '))
            choice_month = int(input('원하는 날짜의 월을 입력해 주세요. (ex : 5) : '))
            choice_day = int(input('원하는 날짜의 일자를 입력해 주세요. (ex : 1) : '))
            make_time(Room_name, choice_year, choice_month, choice_day)
            time = int(input('원하는 시간을 선택해 주세요. (ex : 14) : '))
            name = input('예약자분의 성함을 입력해 주세요. : ')
            number_of_people = int(input('이용하실 분들의 총 인원수를 숫자로 입력해 주세요. (ex : 5) : '))
            password = str(input('비밀번호 4자리를 설정해주세요. (ex : 2012) : '))
            f.write(f'{choice_year},{choice_month},{choice_day},{time},{name},{number_of_people},{str(password)}\n')
            print(f'{name}님 외 {number_of_people-1}분\n{choice_year}년 {choice_month}월 {choice_day}일 {time}시 ~ {time+1}시 <Double> 회의실 예약 완료 되었습니다.')
    
    else: 
        print('등록되지 않은 방 번호 입니다.')

def del_(Room_name):
        Room_name_str = str(Room_name)
        Room_name_list = []
        with open(f'{Room_name_str}.csv', 'r') as f:
                lines = f.readlines()
                for line in lines[1:]:
                        line = line.strip()
                        Room_name_list.append(line.split(","))

        del_name = input('취소하실 예약자분의 성함을 입력해 주세요. : ')
        name_list = []
        for i in range(len(Room_name_list)):
               name_list.append(Room_name_list[i][4])
        if del_name not in name_list:
               print('예약된 정보가 없습니다.')
        else:
                for i in Room_name_list:
                        if del_name == i[4]:
                                print(f'{i[0]}년 {i[1]}월 {i[2]}일 {i[3]}시 예약한 {i[4]}님의 예약을 취소하시려면 비밀번호 4자리를 입력해 주세요.')
                                password = str(input('비밀번호 입력 : '))
                                if password == i[6]:
                                        print(f'{i[4]}님의 예약이 정상적으로 취소되었습니다.')
                                        Room_name_list.remove(i)
                                else:
                                        print('비밀번호가 틀렸습니다.')
                        else:
                                continue
                with open(f'{Room_name_str}.csv', 'w') as f:
                        f.write('년도,월,일,시간,이름,인원,비밀번호\n')
                        for i in range(len(Room_name_list)):
                                f.write(f'{Room_name_list[i][0]},{Room_name_list[i][1]},{Room_name_list[i][2]},{Room_name_list[i][3]},{Room_name_list[i][4]},{Room_name_list[i][5]},{Room_name_list[i][6]}\n')

def Info(Room_name):
    Room_name_str = str(Room_name)
    Room_name_list = []
    with open(f'{Room_name_str}.csv', 'r') as f:
        lines = f.readlines()
        for line in lines[1:]:
            line = line.strip()
            Room_name_list.append(line.split(","))
    info_name = input('예약 확인하실 예약자분의 성함을 입력해 주세요. : ')
    name_list = []
    for i in range(len(Room_name_list)):
        name_list.append(Room_name_list[i][4])
    if info_name in name_list:    
        for i in range(len(Room_name_list)):
            if Room_name_list[i][4] == info_name:
                print(f'{Room_name_list[i][4]}님외 {Room_name_list[i][5]}분은 {Room_name_list[i][0]}년 {Room_name_list[i][1]}월 {Room_name_list[i][2]}일 {Room_name_list[i][3]}시 부터 {int(Room_name_list[i][3])+1}시까지 {Room_name_str}회의실에 예약되어 있습니다.')
            else:
                continue
    else:
        print('예약된 정보가 없습니다.')

def again(Room_name):
        Room_name_str = str(Room_name)
        Room_name_list = []
        with open(f'{Room_name_str}.csv', 'r') as f:
                lines = f.readlines()
                for line in lines[1:]:
                        line = line.strip()
                        Room_name_list.append(line.split(","))
        import copy
        copy_list = copy.deepcopy(Room_name_list)
        del_name = input('취소하실 예약자분의 성함을 입력해 주세요. : ')
        name_list = []
        for i in range(len(Room_name_list)):
               name_list.append(Room_name_list[i][4])
        if del_name not in name_list:
               print('예약된 정보가 없습니다.')
        else:
                for i in Room_name_list:
                        if del_name == i[4]:
                                print(f'{i[0]}년 {i[1]}월 {i[2]}일 {i[3]}시 예약한 {i[4]}님의 예약을 취소하시려면 비밀번호 4자리를 입력해 주세요.')
                                password = str(input('비밀번호 입력 : '))
                                if password == i[6]:
                                        print(f'{i[4]}님의 예약이 정상적으로 취소되었습니다.')
                                        print(f'{i[4]}님의 새로운 예약 도와드리겠습니다.')
                                        copy_list.remove(i)

                                else:
                                        print('비밀번호가 틀렸습니다.')
                        else:
                                continue
                with open(f'{Room_name_str}.csv', 'w') as f:
                        f.write('년도,월,일,시간,이름,인원,비밀번호\n')
                        for i in range(len(copy_list)):
                                f.write(f'{copy_list[i][0]},{copy_list[i][1]},{copy_list[i][2]},{copy_list[i][3]},{copy_list[i][4]},{copy_list[i][5]},{copy_list[i][6]}\n')
        if len(Room_name_list) != len(copy_list):
               room_choice()

prompt='''
    ==================================
    =                                =
    =     <회의실 예약 프로그램>     =
    =                                =
    =     1. 파일 생성 및 초기화     =
    =       2. 예약내역 조회         =
    =       3. 새로 예약하기         =
    =       4. 예약 취소하기         =
    =       5. 예약 수정하기         =
    =          6. 끝내기             = 
    =                                =
    ==================================

'''

num = 0

while num !=6:
        print(prompt)
        num = int(input('실행 할 프로그램의 번호를 입력해 주세요. : '))
        if num == 1:
                new_room_file()

        elif num == 2:
                try:
                        Room_num = int(input('예약내역 조회 할 회의실을 선택해 주세요.\n1. Lets\n2. Rolling\n3. Double\n회의실 번호로 입력해 주세요. (ex : 1) : '))
                        if Room_num == 1:
                                Info('Lets')
                        elif Room_num == 2:
                                Info('Rolling')
                        elif Room_num == 3:
                                Info('Double')
                        else:
                                print('등록되지 않은 회의실 번호 입니다.')
                except FileNotFoundError:
                       print('회의실 파일을 먼저 생성해 주세요.')
        elif num == 3:
                try:
                        room_choice()
                except FileNotFoundError:
                       print('회의실 파일을 먼저 생성해 주세요.')
                
        elif num == 4:
                try:
                        Room_num = int(input('1. Lets\n2. Rolling\n3. Double\n취소하실 회의실의 번호를 입력해주세요. (ex : 1) : '))
                        if Room_num == 1 :
                                Room = 'Lets'
                        elif Room_num == 2:
                                Room = 'Rolling'
                        elif Room_num == 3:
                                Room = 'Double'
                        else:
                                print('등록되지 않은 회의실 번호입니다.')
                        del_(Room)
                except FileNotFoundError:
                       print('회의실 파일을 먼저 생성해 주세요.')
        
        elif num == 5:
                try:
                        print('예약된 정보 삭제 후 신규 예약으로 예약수정이 진행됩니다.')
                        Room_num = int(input('1. Lets\n2. Rolling\n3. Double\n취소하실 회의실의 번호를 입력해주세요. (ex : 1) : '))
                        if Room_num == 1 :
                                Room = 'Lets'
                        elif Room_num == 2:
                                Room = 'Rolling'
                        elif Room_num == 3:
                                Room = 'Double'
                        else:
                                print('등록되지 않은 회의실 번호입니다.')
                        again(Room)
                except FileNotFoundError:
                       print('회의실 파일을 먼저 생성해 주세요.')
        elif num == 6:
                break
        else:
               print('번호를 올바르게 입력해 주세요.')
