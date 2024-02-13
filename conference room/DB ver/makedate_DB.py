from datetime import *
from time import *
from DTO import *

def makedate(Room_name):
        Room_name_str = str(Room_name)
        Room_name_list = ListRoom(Room_name_str)
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
                        daate = da_te.strftime("%Y-%m-%d")
                        reservation = 0
                        for i in range(len(Room_name_list)):
                                if daate == str(Room_name_list[i][1]):
                                        reservation += 1
                                else:
                                        continue
                        print(f'{daate}({day_week}) : 예약 {reservation} 건')

                                
                elif da_te.strftime('%w') == '2':
                        day_week = '화'
                        daate = da_te.strftime("%Y-%m-%d")
                        reservation = 0
                        for i in range(len(Room_name_list)):
                                if daate == str(Room_name_list[i][1]):
                                        reservation += 1
                                else:
                                        continue
                        print(f'{daate}({day_week}) : 예약 {reservation} 건')
                        
                elif da_te.strftime('%w') == '3':
                        day_week = '수'
                        daate = da_te.strftime("%Y-%m-%d")
                        reservation = 0
                        for i in range(len(Room_name_list)):
                                if daate == str(Room_name_list[i][1]):
                                        reservation += 1
                                else:
                                        continue
                        print(f'{daate}({day_week}) : 예약 {reservation} 건')
                        
                elif da_te.strftime('%w') == '4':
                        day_week = '목'
                        daate = da_te.strftime("%Y-%m-%d")
                        reservation = 0
                        for i in range(len(Room_name_list)):
                                if daate == str(Room_name_list[i][1]):
                                        reservation += 1
                                else:
                                        continue
                        print(f'{daate}({day_week}) : 예약 {reservation} 건')
                        
                elif da_te.strftime('%w') == '5':
                        day_week = '금'
                        daate = da_te.strftime("%Y-%m-%d")
                        reservation = 0
                        for i in range(len(Room_name_list)):
                                if daate == str(Room_name_list[i][1]):
                                        reservation += 1
                                else:
                                        continue
                        print(f'{daate}({day_week}) : 예약 {reservation} 건')

                else:
                        continue
     