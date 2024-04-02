import database


db = database.ConnectionDB(dbname='akimo', host='192.168.0.177', user='sugawara', password='1qw23er4')
data = db.get_data_calibrating()

for i in data:
    deviceid_port = i['deviceid_port'].split('_')
    i['deviceid_port'] = str(int(deviceid_port[0]) // 2) + '_' + deviceid_port[1]

db.connection_close()
db = database.ConnectionDB(dbname='akimo_test_candidat', host='192.168.0.177', user='sugawara', password='1qw23er4')
db.insert_data_calibrating(data=data)
db.connection_close()