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
