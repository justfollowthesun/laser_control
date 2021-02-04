import os
import sqlite3
from config import DB_PATH, DB_DIR
from datetime import datetime, timedelta
from input_data import data_generator

class DataParser():

    def __init__(self):

        if not os.path.exists(DB_DIR):
            os.mkdir(DB_DIR)


        self.operation_set = ['PROGRAM', 'TASK', 'PAUSE', 'LASER', 'GAS']

    def add_to_db(self) -> None:

        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()

        user_login = InputData().user_login
        machine = InputData().machine

        cursor.execute("""DELETE FROM operations""")
        for data in self.row_data:

            if data[1] in self.operation_set:

                for data_finish in self.row_data[self.row_data.index(data)+1:]:

                    if data_finish[1] == data[1]:

                        operation = data[1]
                        start_time = data[0]
                        finish_time = data_finish[0]

                        insert_line = """INSERT INTO operations (user_login, operation_name, start_operation, finish_operation, machine_name) values(?, ?, ?, ?, ?)"""
                        cursor.execute(insert_line, (user_login, operation, start_time, finish_time, machine))


            else:

                operation = data[1]
                start_time = data[0]
                finish_time = data[0]

                insert_line = """INSERT INTO operations (user_login, operation_name, start_operation, finish_operation, machine_name) values(?, ?, ?, ?, ?)"""
                cursor.execute(insert_line, (user_login, operation, start_time, finish_time, machine))


        connection.commit()
        connection.close()

    def filters(self, start_data, finish_data, users, machines) -> list:

        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()

        filter_list = users + machines + [start_data] + [finish_data]
        start_str = 'SELECT * FROM operations WHERE '
        str_users = ''
        str_machines = ''
        i, j =0, 0

        while i < len(users)-1:

            i = i + 1
            str_users =  str_users + 'user_login=? OR '

        str_users = str_users + 'user_login=?'

        while j < len(machines)-1:

            j = j + 1
            str_machines = str_machines + 'machine_name=? OR '

        str_machines = str_machines + 'machine_name=?'

        execute_line = start_str + '(' + str_users + ')'+ ' AND ' + '(' + str_machines + ')'+ ' AND ' + 'start_operation>=?'+ ' AND ' + 'finish_operation<=?'

        cursor.execute(execute_line, filter_list)
        filtered_data = cursor.fetchall()
        connection.commit()
        connection.close()
        return filtered_data

    def machines(self) -> list:

        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        cursor.execute("SELECT machine_name FROM machines ")
        machines = cursor.fetchall()
        connection.commit()
        connection.close()
        machines_res =[]
        for machine in machines:

            machines_res.append(machine[0])

        return machines_res

    def users(self) -> list:

        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        cursor.execute("SELECT user_name FROM users ")
        users = cursor.fetchall()
        connection.commit()
        connection.close()
        users_res =[]
        for user in users:

            users_res.append(user[0])

        return users_res

    def date_to_table(self, start_data, finish_data, users, machines) -> dict:

        d = {}
        program_time = 0
        for operation in self.operation_set:
            d[operation] = 0

        row_data = self.filters(start_data, finish_data, users, machines)
        print(row_data)
        for data in row_data:

            if data[2] in self.operation_set:

                datetime_start = datetime.strptime(data[3], '%Y-%m-%d %H:%M:%S')
                datetime_finish = datetime.strptime(data[4], '%Y-%m-%d %H:%M:%S')

                d[data[2]] = d[data[2]]+ (datetime_finish - datetime_start).seconds


        if d['PROGRAM'] == 0:

            d['PROGRAM'] = (datetime.strptime(row_data[-1][4], '%Y-%m-%d %H:%M:%S') - datetime.strptime(row_data[0][3], '%Y-%m-%d %H:%M:%S')).seconds

        return d

    def parsing(self):

        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        gen_data = data_generator()
        list_to_pars = next(gen_data)

        event_date = list_to_pars[0]
        user = list_to_pars[1]
        machine = list_to_pars[2]
        event = list_to_pars[3]
        status = list_to_pars[4]

        cursor.execute(f"""SELECT * FROM users WHERE user_name = ? """, (user,))


        if not cursor.fetchone():

            insert_line = """INSERT INTO users VALUES (NULL, ?) """
            cursor.execute(insert_line, (user, ))
            connection.commit()

        cursor.execute(f"""SELECT * FROM machines WHERE machine_name = ? """, (machine,))

        if  not cursor.fetchone():

            insert_line = '''INSERT INTO machines VALUES (NULL, ?) '''
            cursor.execute(insert_line, (machine,))
            connection.commit()

        cursor.execute(f"""SELECT * FROM status_table WHERE status_name = ? """, (status,))

        if  not cursor.fetchone():
            insert_line = """INSERT INTO status_table  VALUES (NULL, ?) """
            cursor.execute(insert_line, (status,))
            connection.commit()

        user_id = cursor.execute(f"""SELECT user_id FROM users WHERE user_name = ? """, (user,)).fetchone()[0]
        machine_id = cursor.execute(f"""SELECT machine_id FROM machines WHERE machine_name = ? """, (machine,)).fetchone()[0]
        status_id = cursor.execute(f"""SELECT status_id FROM status_table WHERE status_name = ? """, (status,)).fetchone()[0]

        print(event_date, user_id, machine_id, event, status_id)

        insert_line = """INSERT INTO operations (event_date, user_id, machine_id, operation, status_id) VALUES (?, ?, ?, ?, ?)"""
        cursor.execute(insert_line, (event_date, user_id, machine_id, event, status_id))
        connection.commit()

        list_to_gui = [event_date, event, status]

        return list_to_gui


test_users = ['User_1', 'User_2']
test_machines = ['Machine_1']

test_parser = DataParser()
#test_parser.add_to_db()
#test_parser.date_to_table('2020-12-01 10:00:00', '2020-12-01 10:07:30', test_users, test_machines)
#test_parser.machines()
#test_parser.users()
test_parser.parsing()
