from DTO import *
from makedate_DB import *
from maketime_DB import *

def againList(date, time, phonenum, name, people, Roomname):
  Alist = [date, time, phonenum, name, people, Roomname]
  print("회의실 변경부터 도와드리겠습니다.")
  print("현재 예약된 회의실은 %s 입니다." %(Roomname))
  room = int(input('1. RoomA\n2. RoomB\n3. RoomC\n4. RoomD\n5. RoomE\n예약하실 회의실의 번호를 입력해주세요. 변경하지 않으시려면 1~5번을 제외한 다른 번호를 입력해주세요.(ex : 1) : '))
  Room_name = Roomname
  if room == 1:
    Room_name = 'RoomA'
  elif room == 2:
    Room_name = 'RoomB'
  elif room == 3:
    Room_name = 'RoomC'
  elif room == 4:
    Room_name = 'RoomD'
  elif room == 5:
    Room_name = 'RoomE'
  Alist[5] = Room_name
  num1 = input("시간 및 날짜 변경을 하시겠습니까?\n변경하시려면 '1'번, 변경하지 않으시려면 '2'번을 눌러주세요. : ")
  if num1 == 1:
    roomAList = ListRoom(Room_name)
    makedate(Room_name)
    choice_year = input('원하는 날짜의 년도를 입력해 주세요. (ex : 2000) : ')
    choice_month = input('원하는 날짜의 월을 입력해 주세요. (ex : 5) : ')
    choice_day = input('원하는 날짜의 일자를 입력해 주세요. (ex : 1) : ')
    date1 = choice_year+choice_month+choice_day
    make_time(Room_name, date1)
    time1 = int(input('원하는 시간을 선택해 주세요. (ex : 14) : '))
    if (checktime(date1, time1, Room_name)):
      Alist[0] = date1
      Alist[1] = time1*10000
    else:
         print("잘못된 시간 입력으로 날짜 변경 없이 진행됩니다.") 
  elif num1 == 2:
    print("%s %s시 ~ %s시로 시간 및 날짜 변경 없이 진행됩니다.")
  else:
    print("올바른 번호를 입력해주세요.")
  
  phonum = input("기존 입력된 번호는 %s입니다. 변경하시려면 변경할 전화번호를 양식에 맞게 입력해주세요. 변경하지 않으시려면 '501'을 입력해주세요.\nex) 010-1111-1111 : " %(phonenum))
  if phonum != 501 :
    Alist[2] = phonum
  
  newname = input("기존 입력된 이름은 %s입니다. 변경하시려면 변경할 이름을 양식에 맞게 입력해주세요. 변경하지 않으시려면 '501'을 입력해주세요. : " %(name))
  
  if newname != 501 :
    Alist[3] = newname

  newple = int(input("기존 예약된 인원은 %s분 입니다. 변경하시려면 변경할 인원을 숫자로 입력해주세요. 변경하지 않으시려면 '501'을 입력해주세요. : "))

  if newple != 501 :
    Alist[4] = newple


  return Alist