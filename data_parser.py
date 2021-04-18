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
    #data_signal = pyqtSignal()
    def __init__(self):

        if not os.path.exists(DB_DIR):
            os.mkdir(DB_DIR)
        #self.data_recieve()
        #self.list = self.data.data_to_pars()
        #self.data_signal = pyqtSignal(self.list)
        self.operations_d = defaultdict(list)
        self.data_signal = 0
        self.data = [None, None, None]

    def parsing_message(self, message):

        msg_to_pars = codecs.decode(message, 'UTF-8')
        msg_to_pars = msg_to_pars[1 : -1]
        msg_to_list = msg_to_pars.split(',')
        data = []
        for msg in msg_to_list:
            msg = msg.split(':"')
            msg = msg[-1][0:-1]
            data.append(msg)
        return data

    def ip_connect(self):

        HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
        PORT = 12345       # Port to listen on (non-privileged ports are > 1023)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

            s.bind((HOST, PORT))
            s.listen()
            conn, addr = s.accept()
            msg_size = 0
            with conn:
                residual_message = ''
                print('Connected by', addr)
                while True:
                    request = conn.recv(1024)
                    if msg_size == 0:
                        if len(request) < 2:
                            pass
                        else:
                            len_message = int.from_bytes(request[:2], 'big')
                            print(len_message)
                            if len(request) < len_message:
                                pass
                            else:
                                while len(request) >= len_message:
                                    len_message = int.from_bytes(request[:2], 'big')

                                    msg_to_pars = request[2:len_message+1]
                                    data = self.parsing_message(msg_to_pars)
                                    self.data_signal = 1
                                    self.parsing(data)
                                    msg_size = 0
                                    request = request[len_message+2:]
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
        cursor.execute("SELECT user_name FROM users ")

        list_to_pars = data
        event_date = list_to_pars[0]
        user = list_to_pars[3]
        machine = 'ML_35'
        event = list_to_pars[1]
        status = list_to_pars[2]

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
        self.data = [event, event_date, status]

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
        cursor.execute(str_users_search, (users))
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

        filter_list.append(datetime.strftime(start_dtime, '%Y-%m-%d %H:%M:%S.%f'))
        filter_list.append(datetime.strftime(finish_dtime, '%Y-%m-%d %H:%M:%S.%f'))
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

        execute_line = start_str + '(' + str_users + ')'+ ' AND ' + 'event_date>=?'+ ' AND ' + 'event_date<=?'
        cursor.execute(execute_line, (filter_list))
        row_filters_data = cursor.fetchall()

        result_data = defaultdict(list)

        start_status = cursor.execute('SELECT status_id FROM status_table WHERE status_name = ?',('START', )).fetchall()
        finish_status = cursor.execute('SELECT status_id FROM status_table WHERE status_name = ?',('FINISH', )).fetchall()

        for lst in row_filters_data:

            result_data[lst[3]].append([lst[0], lst[4]])


        sorted_data = defaultdict(list)
        error_data = defaultdict(list)

        for operation in result_data.keys():

            start_operation_str = result_data[operation][0][0]
            start_operation_date = datetime.strptime(start_operation_str, '%Y-%m-%d %H:%M:%S.%f')
            if operation == 'ERROR':
                error_id = result_data[operation][-1][-1]
                error_name  = cursor.execute('SELECT status_name FROM status_table WHERE status_id= ?',(error_id, )).fetchall()
                error_data[error_name[0][0]] = start_operation_str
            elif operation != 'ERROR' and int(result_data[operation][-1][-1]) == finish_status[0][0]:
                end_operation_str = result_data[operation][-1][-2]
                end_operation_date = datetime.strptime(end_operation_str, '%Y-%m-%d %H:%M:%S.%f')
                time_sec = (end_operation_date - start_operation_date).total_seconds()
                sorted_data[operation] = time_sec

            elif operation != 'ERROR' and int(result_data[operation][-1][-1]) == start_status[0][0]:
                end_operation_str = finish_dtime
                end_operation_date = finish_dtime
                time_sec = (end_operation_date - start_operation_date).total_seconds()
                sorted_data[operation] = time_sec


        connection.commit()
        connection.close()

        return sorted_data, error_data

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


# test_users = ['User_1', 'User_2']
# test_machines = ['Machine_1']
#
test_parser = DataParser()

# for event in list_of_events:
#
#     test_parser.parsing(event)
# test_parser.hours_from_user('User_1')
