def Info(Room_name):
    Room_name_str = str(Room_name)
    Room_name_list = []
    with open(f'{Room_name_str}.csv', 'r') as f:
        lines = f.readlines()
        for line in lines[1:]:
            line = line.strip()
            Room_name_list.append(line.split(","))
    info_name = input('예약 확인하실 예약자분의 성함을 입력해 주세요. : ')
    name_list = []
    for i in range(len(Room_name_list)):
        name_list.append(Room_name_list[i][4])
    if info_name in name_list:    
        for i in range(len(Room_name_list)):
            if Room_name_list[i][4] == info_name:
                print(f'{Room_name_list[i][4]}님외 {Room_name_list[i][5]}분은 {Room_name_list[i][0]}년 {Room_name_list[i][1]}월 {Room_name_list[i][2]}일 {Room_name_list[i][3]}시 부터 {Room_name_list[i][3]+1}시까지 {Room_name_str}회의실에 예약되어 있습니다.')
            else:
                continue
    else:
        print('예약된 정보가 없습니다.')