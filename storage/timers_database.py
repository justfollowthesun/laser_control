import os
import logging
import sqlite3
from config import DB_TIMERS_PATH, DB_DIR
from datetime import datetime, timedelta


class Timers_Database():

    def __init__(self) -> None:

        if not os.path.exists(DB_DIR):
            os.mkdir(DB_DIR)

        self.connection = sqlite3.connect(DB_TIMERS_PATH)
        self.cursor = self.connection.cursor()
        self.now = datetime.now()

    def select_data(self) -> str:

        self.cursor.execute("""SELECT * FROM timers """)
        result = self.cursor.fetchall()
        print(result)
        # comment = result[3]
        # alg_to_solve = result[4]
        # datetime_object = datetime.strptime(result[1], '%Y/%m/%d/%H/%M/%S')
        #
        # time_delta = datetime_object-self.now
        # days, remainder = divmod(time_delta.seconds, 86400)
        # hours, remainder = divmod(remainder, 3600)
        # minutes, seconds = divmod(remainder, 60)
        return result

    def reset_timer_data(self, timer_id) -> None:

        self.cursor.execute("SELECT rate_to_change FROM timers WHERE operation_id = ? ",(timer_id,))
        result = self.cursor.fetchone()

        days_to_change = result[0]

        now = datetime.strftime(datetime.now(), '%Y/%m/%d/%H/%M/%S')

        new_data = datetime.now() + timedelta(days = days_to_change)

        new_data_str = datetime.strftime(new_data, '%Y/%m/%d/%H/%M/%S')
        self.cursor.execute('''UPDATE timers SET date_to_change = ? WHERE operation_id = ?''', (new_data_str, timer_id))
        self.connection.commit()
        print('all right')

    def connect_with_db(self, str_to_search):

        result = self.cursor.execute("SELECT * FROM users WHERE user_name LIKE ?",(str_to_search)).fetchall()
        return result
