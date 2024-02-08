from DTO import *
from makedate_DB import *
from maketime_DB import *

def room_choice():
    room = int(input('1. RoomA\n2. RoomB\n3. RoomC\n4. RoomD\n5. RoomE\n예약하실 회의실의 번호를 입력해주세요. (ex : 1) : '))
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
      roomAList = ListRoom(Room_name)
      makedate(Room_name)
      choice_year = input('원하는 날짜의 년도를 입력해 주세요. (ex : 2000) : ')
      choice_month = input('원하는 날짜의 월을 입력해 주세요. (ex : 5) : ')
      choice_day = input('원하는 날짜의 일자를 입력해 주세요. (ex : 1) : ')
      date = choice_year+choice_month+choice_day
      make_time(Room_name, date)
      time = int(input('원하는 시간을 선택해 주세요. (ex : 14) : '))
      if (checktime(date, time, Room_name)):
        name = input('예약자분의 성함을 입력해 주세요. : ')
        phonenum = input('예약자분의 전화번호를 입력해주세요. (ex : 010-0000-0000) : ')
        number_of_people = int(input('이용하실 분들의 총 인원수를 숫자로 입력해 주세요. (ex : 5) : '))
        password = str(input('비밀번호 4자리를 설정해주세요. (ex : 2012) : '))
        InsertRoom(Room_name, date, time*10000, phonenum, name, number_of_people, password)
        print(f'{name}님 외 {number_of_people-1}분\n{choice_year}년 {choice_month}월 {choice_day}일 {time}시 ~ {time+1}시 <{Room_name}> 회의실 예약 완료 되었습니다.')
      else:
         print("잘못된 시간 입력으로 예약이 종료됩니다.") 
    else: 
        print('등록되지 않은 방 번호 입니다.')


