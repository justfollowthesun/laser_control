import os
import sqlite3
import socket
import codecs
import threading
from config import DB_PATH, DB_DIR
from datetime import datetime, timedelta
from input_data import data_generator
from PyQt5.QtCore import QSize, Qt, QThread, pyqtSignal, QTimer
from collections import defaultdict


class DataParser():

    def __init__(self):

        if not os.path.exists(DB_DIR):
            os.mkdir(DB_DIR)
        #self.data_recieve()
        #self.list = self.data.data_to_pars()
        #self.data_signal = pyqtSignal(self.list)
        self.operations_d = defaultdict(list)
        self.msg_status = 1
        # x = threading.Thread(target = self.ip_connect)
        # x.start()

    def ip_connect(self):

        HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
        PORT = 12345       # Port to listen on (non-privileged ports are > 1023)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

            s.bind((HOST, PORT))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    request = conn.recv(1024)
                    msg_size = 0
                    if msg_size == 0:
                        if len(request) < 2:
                            pass
                        else:
                            len_message = int.from_bytes(request[:2], 'big')

                            if len(request) < len_message:
                                pass
                            else:
                                message = request[2:]
                                message = codecs.decode(message, 'UTF-8')
                                message = message[1 : -1]
                                msg_to_list = message.split(',')
                                print(msg_to_list)
                                data = []

                                for msg in msg_to_list:
                                    msg = msg.split(':"')
                                    msg = msg[-1][0:-1]
                                    data.append(msg)
                                    msg_size == 0
                                    self.msg_status = 1
                    print(data)
                    self.parsing(data)
                    if not data:
                        break

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

    def parsing(self, data):

        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        gen_data = data_generator()
        list_to_pars = data

        event_date = list_to_pars[0]
        print(event_date)
        user = list_to_pars[4]
        machine = list_to_pars[1]
        event = list_to_pars[2]
        status = list_to_pars[3]

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
        insert_line = """INSERT INTO operations (event_date, user_id, machine_id, operation, status_id) VALUES (?, ?, ?, ?, ?)"""
        cursor.execute(insert_line, (event_date, user_id, machine_id, event, status_id))
        connection.commit()
        self.operations_d[event].append([event_date, status])

    # def date_for_table(self):
    #
    #     connection = sqlite3.connect(DB_PATH)
    #     cursor = connection.cursor()
    #     cursor.execute("SELECT * FROM operations ")








    def data_from_filters(self, start_dtime, finish_dtime, users, equipment):

        i, j = 0, 0
        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()
        str_users = ''
        str_machines =''

        while i < len(users) - 1:
            i = i + 1
            str_users =  str_users + 'user_name = ? OR '

        str_users = str_users + 'user_name = ?'
        str_users_search = 'SELECT user_id FROM users WHERE ' + str_users
        cursor.execute(str_users_search, users)
        users = cursor.fetchall()

        while j < len(equipment) - 1:
            j = j + 1
            str_machines = str_machines + 'machine_name = ? OR '

        str_machines = str_machines + 'machine_name = ?'
        str_machines_search = 'SELECT machine_id FROM machines WHERE ' + str_machines

        cursor.execute(str_machines_search, equipment)
        machines = cursor.fetchall()

        filter_list = []
        for user in users:
            filter_list.append(user[0])

        for machine in machines:
            filter_list.append(machine[0])

        filter_list.append(datetime.strftime(start_dtime, '%Y-%m-%d %H:%M:%S'))
        filter_list.append(datetime.strftime(finish_dtime, '%Y-%m-%d %H:%M:%S'))
        start_str = 'SELECT * FROM operations WHERE '
        str_users = ''
        str_machines = ''
        i, j =0, 0

        while i < len(users)-1:

            i = i + 1
            str_users =  str_users + 'user_id = ? OR '
        str_users = str_users + 'user_id=?'

        while j < len(machines)-1:

            j = j + 1
            str_machines = str_machines + 'machine_id=? OR '

        str_machines = str_machines + 'machine_id=?'

        execute_line = start_str + '(' + str_users + ')'+ ' AND ' + '(' + str_machines + ')'+ ' AND ' + 'event_date>=?'+ ' AND ' + 'event_date<=?'
        cursor.execute(execute_line, filter_list)

        row_filters_data = cursor.fetchall()

        result_data = defaultdict(list)

        start_status = cursor.execute('SELECT status_id FROM status_table WHERE status_name = ?',('START', )).fetchall()
        finish_status = cursor.execute('SELECT status_id FROM status_table WHERE status_name = ?',('FINISH', )).fetchall()

        #print(row_filters_data)

        for lst in row_filters_data:

            result_data[lst[3]].append([lst[0], lst[4]])

        sorted_data = defaultdict(list)
        print(row_filters_data)

        for operation in result_data.keys():

            if int(result_data[operation][-1][-1]) == finish_status[0][0]:

                end_operation_str = result_data[operation][-1][-2]
                end_operation_date = datetime.strptime(end_operation_str, '%Y-%m-%d %H:%M:%S')

                start_operation_str = result_data[operation][0][0]
                start_operation_date = datetime.strptime(start_operation_str, '%Y-%m-%d %H:%M:%S')

                time_sec = (end_operation_date - start_operation_date ).total_seconds()
                sorted_data[operation] = time_sec

        connection.commit()
        connection.close()
        return sorted_data

    def hours_from_user(self, user:str) -> int:

        '''
        Return number of hour for choisen user
        '''

        connection = sqlite3.connect(DB_PATH) #connect to database
        cursor = connection.cursor()

        cursor.execute("SELECT user_id FROM users WHERE user_name=?", (user,)) #select id from choisen user
        id = cursor.fetchone()

        cursor.execute("SELECT event_date FROM operations WHERE user_id = ?", (id[0], ))

        dtime_for_user = cursor.fetchall()

        summ = 0
        start_dtime_str = dtime_for_user[0]

        start_dtime = datetime.strptime(start_dtime_str[0], '%Y-%m-%d %H:%M:%S') #convert to python datetime start datetime in the selected values from operation table

        for dtime in dtime_for_user:

            python_dtime = datetime.strptime(dtime[0], '%Y-%m-%d %H:%M:%S')
            sec_to_append = (python_dtime - start_dtime).total_seconds()
            summ = summ + sec_to_append

        connection.commit()
        connection.close()
        total_hours = int(summ/3600)

    def hours_from_machine(self, machine:str) -> int:

        '''
        Return number of hour for choisen user
        '''

        connection = sqlite3.connect(DB_PATH) #connect to database
        cursor = connection.cursor()

        cursor.execute("SELECT machine_id FROM machines WHERE machine_name=?", (user,)) #select id from choisen user
        id = cursor.fetchone()

        cursor.execute("SELECT event_date FROM operations WHERE machine_id = ?", (id[0], ))

        dtime_for_machine= cursor.fetchall()

        summ = 0
        start_dtime_str = dtime_for_machine[0]

        start_dtime = datetime.strptime(start_dtime_str[0], '%Y-%m-%d %H:%M:%S') #convert to python datetime start datetime in the selected values from operation table

        for dtime in dtime_for_machine:

            python_dtime = datetime.strptime(dtime[0], '%Y-%m-%d %H:%M:%S')
            sec_to_append = (python_dtime - start_dtime).total_seconds()
            summ = summ + sec_to_append

        connection.commit()
        connection.close()
        total_hours = int(summ/3600)

list_of_events = [
    ["2020-12-01 09:00:00", 'User_2', 'Machine_1', 'PROGRAM', 'START'],
    ["2020-12-01 10:05:00", 'User_1', 'Machine_1', 'TASK', 'START'],
    ["2020-12-01 10:05:00", 'User_1', 'Machine_1', 'LASER', 'START'],
    ["2020-12-01 10:05:30", 'User_2', 'Machine_1', 'GAS', 'START'],
    ["2020-12-01 10:06:30", 'User_2', 'Machine_1', 'GAS', 'FINISH'],
    ["2020-12-01 10:07:00", 'User_1', 'Machine_1',  'LASER', 'FINISH'],
    ["2020-12-01 10:07:30", 'User_1', 'Machine_1', 'ERROR_1', 'FINISH'],
    ["2020-12-01 10:09:00", 'User_1', 'Machine_1',  'TASK', 'FINISH'],
    ["2020-12-01 10:30:00", 'User_1', 'Machine_1', 'PROGRAM', 'FINISH']
        ]


# test_users = ['User_1', 'User_2']
# test_machines = ['Machine_1']
#
test_parser = DataParser()

# for event in list_of_events:
#
#     test_parser.parsing(event)
# test_parser.hours_from_user('User_1')
