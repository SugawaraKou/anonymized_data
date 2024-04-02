import database
import random


db = database.ConnectionDB(dbname='akimo', host='192.168.0.177', user='sugawara', password='1qw23er4')
data = db.get_data_messages()


for i in data:
    try:
        i['terminal_id'] = str(int(i['terminal_id']) // 2)
    except:
        continue
    try:
        i['lat'] = i['lat'] + 2
        i['lon'] = i['lon'] + 2
        i['course'] = i['course'] + 2
        i['alt'] = i['alt'] + 2
        i['satellites'] = i['satellites'] + 1
    except:
        i['lat'] = random.randint(0, 150)
        i['lon'] = random.randint(0, 150)
        i['course'] = random.randint(0, 300)
        i['alt'] = random.randint(0, 150)
        i['satellites'] = random.randint(0, 15)

db.connection_close()
db = database.ConnectionDB(dbname='akimo_test_candidat', host='192.168.0.177', user='sugawara', password='1qw23er4')
db.insert_data_messages(data=data)
db.connection_close()
