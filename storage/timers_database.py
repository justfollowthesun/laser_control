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

    def select_data(self, operation_name:str) -> str:

        self.cursor.execute("SELECT * FROM timers WHERE operation = ? ",(operation_name,))
        result = self.cursor.fetchone()
        datetime_object = datetime.strptime(result[1], '%Y/%m/%d/%H/%M/%S')

        time_delta = datetime_object-self.now
        days, remainder = divmod(time_delta.seconds, 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)
        return '{:02}:{:02}:{:02}'.format(int(time_delta.days), int(hours), int(minutes))

    def reset_timer_data(self, operation_name: str) -> None:

        self.cursor.execute("SELECT rate_to_change FROM timers WHERE operation = ? ",(operation_name,))
        result = self.cursor.fetchone()
        date = result[0]
        now = datetime.now().strftime('%Y/%m/%d/%H/%M/%S')
        date_res = []

        for now, date in zip(now.split('/'), date.split('/')):

            date_res.append(str(int(now)+ int(date)))

        self.cursor.execute('''UPDATE timers SET date_to_change = ? WHERE operation = ?''', ('/'.join(date_res), operation_name))
        self.connection.commit()
