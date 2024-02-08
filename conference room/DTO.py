import pymysql

conn = pymysql.connect(host = '13.124.144.111', user = 'usrid', password = 'usrpassword', db = 'ConferenceRoom', charset = 'utf8')

cur = conn.cursor()

def ListRoom(Roomname):
  sql = "SELECT * FROM %s" %(Roomname)
  cur.execute(sql)
  b = list()
  for row in cur:
    a=list()
    a.append(row[0])
    a.append(row[1])
    a.append(row[2])
    a.append(row[3])
    a.append(row[4])
    a.append(row[5])
    a.append(row[6])
    b.append(a)
  return b
    
def InsertRoom(Roomname, date, time, phonenum, name, people, password):
  sql = "INSERT INTO %s (resdate, restime, phonenum, resname, people, respassword) VALUE ('%s', '%s', '%s', '%s', '%s', '%s');" %(Roomname,date, time, phonenum, name, people, password)
  cur.execute(sql)
  conn.commit()
  print("%s님의 예약이 완료되었습니다." %(name))

def DeleteRoom(Roomname,name, id):
  sql = "DELETE FROM %s WHERE id = '%s';" %(Roomname,id)
  cur.execute(sql)
  conn.commit()
  print("%s님의 예약이 취소되었습니다."%(name))

def UpdateRoom(Roomname,date, time, phonenum, name, people, password, id):
  sql = "UPDATE %s SET resdate='%s', restime='%s', phonenum='%s', resname='%s', people='%s', respassword='%s' WHERE id = '%s';" %(Roomname,date, time, phonenum, name, people, password, id)
  cur.execute(sql)
  conn.commit()
  print("%s님의 예약이 수정되었습니다."%(name))


