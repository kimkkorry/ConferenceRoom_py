from DTO import *

def del_(Room_name):
        Room_name_str = str(Room_name)
        Room_name_list = ListRoom(Room_name_str)

        del_name = input('취소하실 예약자분의 성함을 입력해 주세요. : ')
        name_list = []
        Same_name_list = []

        for i in range(len(Room_name_list)):
               name_list.append(Room_name_list[i][4])

        if del_name not in name_list:
                print('예약된 정보가 없습니다.')
        else:
                for i in Room_name_list:
                        if del_name == i[4]:
                                if name_list.count(del_name) >1 :
                                        Same_name_list.append(i)
                                else:
                                        time1 = str(i[2])[:2].replace(':', '')
                                        print("%s %s시 ~ %s시 예약한 %s님의 예약을 취소하시려면 비밀번호 4자리를 입력해 주세요." %(i[1], time1, int(time1)+1, i[4]))
                                        password = str(input('비밀번호 입력 : '))
                                        id = 0
                                        for j in Room_name_list:
                                                if i[4] == j[4] :
                                                        id = j[0]

                                        if password == i[6]:
                                                print(f'{i[4]}님의 예약이 정상적으로 취소되었습니다.')
                                                DeleteRoom(Room_name_str, i[4], id)
                                        else:
                                                print('비밀번호가 틀렸습니다.')
                
                if len(Same_name_list) >0:
                                        SameId = []
                                        for i in Same_name_list:
                                               time1 = str(i[2])[:2].replace(':', '')
                                               print("%s. %s %s시 ~ %s시 예약한 %s님 외 %s분\n " %(i[0], i[1], time1, int(time1)+1, i[4], i[5]))
                                               SameId.append(i[0])
                                                
                                        Same_name_choice = int(input('예약 취소할 분의 번호를 입력해 주세요. (ex : 1) : '))
                                        for i in Room_name_list:
                                                if Same_name_choice not in SameId:
                                                        print("올바른 번호를 입력해주세요.")
                                                else:
                                                        time1 = str(i[2])[:2].replace(':', '')
                                                        if Same_name_choice == int(i[0]):
                                                                print("%s %s시 ~ %s시 예약한 %s님의 예약을 취소하시려면 비밀번호 4자리를 입력해 주세요." %(i[1], time1, int(time1)+1, i[4]))
                                                                password = str(input('비밀번호 입력 : '))
                                                                if password == i[6]:
                                                                        print(f'{i[4]}님의 예약이 정상적으로 취소되었습니다.')
                                                                        DeleteRoom(Room_name_str, i[4], i[0])
                                                                else:
                                                                         print('비밀번호가 틀렸습니다.')

