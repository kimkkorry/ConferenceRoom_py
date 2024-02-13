from DTO import *

def makecsvfile(Roomname) :
  Rlist = ListRoom(Roomname)
  with open("%s.csv"%(Roomname), "w") as f:
    f.write('날짜, 시간, 이름, 전화번호, 인원\n')
    for i in Rlist:
      f.write("%s, %s, %s, %s, %s\n" %(i[1], i[2], i[4], i[3], i[5]))
    f.close()
  print('%s.csv 파일이 해당 폴더에 생성되었습니다.' %(Roomname))