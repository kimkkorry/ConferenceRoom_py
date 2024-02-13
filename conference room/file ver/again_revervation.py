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
        Same_name_list = []
        Same_name_list_2 = []
        for i in range(len(Room_name_list)):
               name_list.append(Room_name_list[i][4])

        with open(f'{Room_name_str}.csv', 'w') as f:
                        f.write('년도,월,일,시간,이름,인원,비밀번호\n')
                        if del_name not in name_list:
                                print('예약된 정보가 없습니다.')
                        else:
                                for i in Room_name_list:
                                        if del_name == i[4]:
                                                if name_list.count(del_name) >1 :
                                                        Same_name_list.append(i)
                                                else:
                                                        print(f'{i[0]}년 {i[1]}월 {i[2]}일 {i[3]}시 예약한 {i[4]}님의 예약을 취소하시려면 비밀번호 4자리를 입력해 주세요.')
                                                        password = str(input('비밀번호 입력 : '))
                                                        if password == i[6]:
                                                                print(f'{i[4]}님의 예약이 정상적으로 취소되었습니다.')
                                                                Room_name_list.remove(i)
                                                                print(f'{del_name}님의 새로운 예약 도와드리겠습니다.')
                                                        else:
                                                                print('비밀번호가 틀렸습니다.')
                                        else:
                                                f.write(f'{i[0]},{i[1]},{i[2]},{i[3]},{i[4]},{i[5]},{i[6]}\n')
                                if Same_name_list != None:
                                        for i in range(len(Same_name_list)):
                                                print(f'{i+1}. {Same_name_list[i][0]}년 {Same_name_list[i][1]}월 {Same_name_list[i][2]}일 {Same_name_list[i][3]}시 예약한 {Same_name_list[i][4]}님 외 {int(Same_name_list[i][5])-1}\n')
                                                SN = []
                                                SN.append(f'{i+1}')
                                                SN.append(f'{Same_name_list[i][0]}')
                                                SN.append(f'{Same_name_list[i][1]}')
                                                SN.append(f'{Same_name_list[i][2]}')
                                                SN.append(f'{Same_name_list[i][3]}')
                                                SN.append(f'{Same_name_list[i][4]}')
                                                SN.append(f'{Same_name_list[i][5]}')
                                                SN.append(f'{Same_name_list[i][6]}')
                                                Same_name_list_2.append(SN)
                                        Same_name_choice = int(input('예약 취소할 분의 번호를 입력해 주세요. (ex : 1) : '))
                                        for i in Same_name_list_2:
                                                if Same_name_choice == int(i[0]):
                                                        print(f'{i[1]}년 {i[2]}월 {i[3]}일 {i[4]}시 예약한 {i[5]}님의 예약을 취소하시려면 비밀번호 4자리를 입력해 주세요.')
                                                        password = str(input('비밀번호 입력 : '))
                                                        if password == i[7]:
                                                                print(f'{i[5]}님의 예약이 정상적으로 취소되었습니다.')
                                                                Same_name_list_2.remove(i)
                                                        else:
                                                                 print('비밀번호가 틀렸습니다.')
                                                                 f.write(f'{i[1]},{i[2]},{i[3]},{i[4]},{i[5]},{i[6]},{i[7]}\n')                                        
                                                else:
                                                        f.write(f'{i[1]},{i[2]},{i[3]},{i[4]},{i[5]},{i[6]},{i[7]}\n')
                                        for i in Same_name_list_2:        
                                                f.write(f'{i[1]},{i[2]},{i[3]},{i[4]},{i[5]},{i[6]},{i[7]}\n')
                        a = input('재예약을 하시려면 1번, 끝내려면 2번을 눌러주세요.\n 숫자입력 : ')
                        if a == 1:
                                room_choice()
                        elif a == 2:
                                print('예약이 취소되었습니다.')
                        else:
                                print('등록되지 않은 번호입니다.')