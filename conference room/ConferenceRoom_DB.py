from ChoiceRoom import *
from againres_DB import *
from delres_DB import *
from info_res_DB import *
from makecsvfile import *

prompt='''
    ==================================
    =                                =
    =     <회의실 예약 프로그램>     =
    =                                =
    =    1. 예약내역 파일 출력하기   =
    =       2. 새로 예약하기         =
    =       3. 예약 취소하기         =
    =       4. 예약 수정하기         =
    =       5. 예약내역 조회         =
    =          6. 끝내기             = 
    =                                =
    ==================================

'''
num = 0

while num != 6:
  print(prompt)
  num = int(input('원하시는 기능의 번호를 입력해주세요. : '))
  if num == 1:
    room = int(input('1. RoomA\n2. RoomB\n3. RoomC\n4. RoomD\n5. RoomE\n출력하실 회의실의 번호를 입력해주세요. (ex : 1) : '))
    Room_name = 'Room'
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

    if Room_name != 'Room' :
      makecsvfile(Room_name)
    else:
      print("올바른 번호를 입력해주세요.")
  elif num == 2:
    room_choice()
  elif num == 3:
    room = int(input('1. RoomA\n2. RoomB\n3. RoomC\n4. RoomD\n5. RoomE\n예약하신 회의실의 번호를 입력해주세요. (ex : 1) : '))
    Room_name = 'Room'
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

    if Room_name != 'Room' :
      del_(Room_name)
    else:
      print("올바른 번호를 입력해주세요.")
  elif num == 4:
    room = int(input('1. RoomA\n2. RoomB\n3. RoomC\n4. RoomD\n5. RoomE\n예약하신 회의실의 번호를 입력해주세요. (ex : 1) : '))
    Room_name = 'Room'
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

    if Room_name != 'Room' :
      update(Room_name)
    else:
      print("올바른 번호를 입력해주세요.")
  elif num == 5:
    room = int(input('1. RoomA\n2. RoomB\n3. RoomC\n4. RoomD\n5. RoomE\n예약하신 회의실의 번호를 입력해주세요. (ex : 1) : '))
    Room_name = 'Room'
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

    if Room_name != 'Room' :
      update(Room_name)
    else:
      print("올바른 번호를 입력해주세요.")
  elif num == 6:
    print("프로그램이 종료됩니다.")
  else:
    print("잘못된 번호입니다.")