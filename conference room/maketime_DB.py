from DTO import *;

def make_time(Room_name, choice_date):
        Room_name_str = str(Room_name)
        Room_name_list = ListRoom(Room_name_str)
        print("%s회의실 %s의 예약가능 시간입니다." %(Room_name_str, choice_date))
        able_time = []
        able_time_2 = []
        for j in range(8,17):
                for i in range(len(Room_name_list)):
                        if j == 12:
                                continue
                        elif str(j) == str(Room_name_list[i][2])[:2]:
                                if choice_date == str(Room_name_list[i][1]).replace('-', '', 2):
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
               print("%s시 ~ %s시" %(i, i+1))

def checktime(date, time, Roomname):
        check = True
        Rlist = ListRoom(Roomname)
        for i in Rlist:
                if str(i[1]).replace('-', '', 2) == date :
                        if int(str(i[2])[:2]) == time:
                                print("이미 예약된 시간입니다.")
                                check = False
        if time<8 and time>17:
                print("이용가능 시간이 아닙니다.")
                check = False
        
        if time == 12 :
                print("점심시간입니다. 다른 시간 이용 부탁드립니다.")
                check = False

        return check