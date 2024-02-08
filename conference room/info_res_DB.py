from DTO import *

def Info(Room_name):
    Room_name_str = str(Room_name)
    Room_name_list = ListRoom(Room_name_str)
    info_name = input('예약 확인하실 예약자분의 성함을 입력해 주세요. : ')
    name_list = []
    for i in range(len(Room_name_list)):
        name_list.append(Room_name_list[i][4])
    if info_name in name_list:    
        for i in Room_name_list:
            if i[4] == info_name:
                print("%s님 (전화번호 뒷자리 : %s) 외 %s분은 %s %s시 부터 %s시 까지 %s 회의실에 예약되어있습니다.\n" %(i[4], i[3][9:], int(i[5]-1), i[1], i[2][:2], int(i[2][:2])+1, Room_name_str))
    else:
        print('예약된 정보가 없습니다.')