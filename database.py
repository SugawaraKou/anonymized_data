import psycopg2
from psycopg2._json import Json


class ConnectionDB:
    def __init__(self, dbname, host, user, password):
        self.connection = psycopg2.connect(f'dbname={dbname} host={host} user={user} password={password}')
        self.cursor = self.connection.cursor()

    def test(self):
        self.cursor.execute(f'select count(*) from akimo_messages')
        result = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in
                  self.cursor.fetchall()]
        return result

    def get_data_messages(self):
        self.cursor.execute(f'select * from akimo_messages')
        result = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()]
        return result

    def get_data_calibrating(self):
        self.cursor.execute(f'select * from akimo_calibrating')
        result = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()]
        return result

    def insert_data_messages(self, data):
        for i in data:
            message_id = i['message_id']
            track_id = i['track_id']
            terminal_id = i['terminal_id']
            lat = i['lat']
            lon = i['lon']
            timestamp = i['timestamp']
            speed = i['speed']
            course = i['course']
            voltage = i['voltage']
            motion = i['motion']
            alt = i['alt']
            source = i['source']
            ignition = i['ignition']
            odometer = i['odometer']
            satellites = i['satellites']
            gsmlevel = i['gsmlevel']
            sensors = i['sensors']
            externals = i['externals']
            outputs = i['outputs']
            can_data = i['can_data']
            temperature = i['temperature']
            created = i['created']
            query = self.cursor.mogrify('INSERT INTO messages values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                                        (message_id, track_id, terminal_id, lat, lon, timestamp, speed, course, voltage,
                                         motion, alt, source, ignition, odometer, satellites, gsmlevel, Json(sensors),
                                         Json(externals), Json(outputs), Json(can_data), Json(temperature), created))
            self.cursor.execute(query)
        self.connection.commit()

    def insert_data_calibrating(self, data):
        for i in data:
            id = i['id']
            deviceid_port = i['deviceid_port']
            calibrating_data = i['calibrating_data']
            query = self.cursor.mogrify('INSERT INTO calibrating values (%s, %s, %s)', (id, deviceid_port, Json(calibrating_data)))
            self.cursor.execute(query)
        self.connection.commit()

    def connection_close(self):
        self.connection.close()