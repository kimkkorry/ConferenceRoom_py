from DTO import *
from againList import *

def update(Room_name):
  Room_name_str = str(Room_name)
  Room_name_list = ListRoom(Room_name_str)

  del_name = input('수정하실 예약자분의 성함을 입력해 주세요. : ')
  name_list = []
  Same_name_list = []
  for i in range(len(Room_name_list)):
    name_list.append(Room_name_list[i][4])
  
  if del_name not in name_list:
    print('예약된 정보가 없습니다.')
  else:
    for i in Room_name_list:
      time1 = str(i[2])[:2].replace(':', '')
      if del_name == i[4]:
        if name_list.count(del_name) >1:
          Same_name_list.append(i)
        else:
          print("%s %s시 ~ %s시 예약한 %s님의 예약을 수정하시려면 비밀번호 4자리를 입력해 주세요." %(i[1], time1, int(time1)+1, i[4]))
          password = str(input('비밀번호 입력 : '))
          id = 0
          for j in Room_name_list:
            if i[4] == j[4] :
              id = j[0]
          if password == i[6]:
            print(f'{i[4]}님 확인 되셨습니다.')
            print("%s 님의 기존 예약 내역입니다." %(i[4]))
            print("날짜 : %s\n시간 : %s시 ~ %s시\n전화번호 : %s\n이름 : %s\n인원수 : 총 %s분\n회의실 : %s\n" %(i[1], time1, int(time1)+1, i[3], i[4], i[5], Room_name_str))
            newList = againList(i[1], i[2], i[3], i[4], i[5], Room_name_str)

            if newList[5] == Room_name_str:
              UpdateRoom(Room_name_str, newList[0], newList[1], newList[2], newList[3], newList[4], i[6], id)
            else:
              DeleteRoom(Room_name_str, i[4], i[0])
              InsertRoom(newList[5], newList[0], newList[1], newList[2], newList[3], newList[4], i[6])
            print("예약 수정이 완료되었습니다.")
          else:
            print('비밀번호가 틀렸습니다.')