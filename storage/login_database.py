
import os
import logging
import sqlite3
# import pandas as pd
from config import DB_LOGIN_PATH, DB_DIR


class Login_Database():

    connection = None

    def __init__(self) -> None:

        if not os.path.exists(DB_DIR):
            os.mkdir(DB_DIR)

        self.connection = sqlite3.connect(DB_LOGIN_PATH)
        self.cursor = self.connection.cursor()

        logging.info("Successfully connect to database")
        logging.info("Successfully load environment")

    def authorization_check(self, login:str, password:str) -> bool:

        self.cursor.execute("SELECT * FROM users WHERE login = ? and password = ?",(login, password,))

        return cursor.fetchone()


    def user_col(self):

        result = self.cursor.execute("SELECT user_name FROM users").fetchall()

        res_list =[]

        for res in result:

            res_list.append(str(res[0]))

        return res_list

    def add_new_user(self, name, login:str, password:str)->None:

        cursor: sqlite3.cursor = self.connection.cursor()
        insert_line = f'insert into {self.tablename} (name,login, password, is_master) values(?, ?, ?, ?)'
        cursor.execute(insert_line, (name, login, password, False))
        self.connection.commit()
        logging.info(f'Have inserted {cursor.rowcount} records to the table.')


    def close(self) -> None:

        if self.connection:
            self.connection.close()
            logging.info("Database connection was closed")


    # def initiate_month(self) -> None:
    #     """Checks if days of the current month are
    #         inserted into database already.
    #         Inserts them if cannot find.
    #     """
    #
    #     today = datetime.now()
        #
        # cursor: sqlite3.Cursor = self.connection.cursor()
        # stored_days_list = self.get_checkboxes( today, cursor=cursor)
        #
        # if not stored_days_list:
        #
    #         insert_line = f'insert into {self.tablename} (id, checked, day, month, full_date) values(?, ?, ?, ?, ?)'
    #         today = today.date()
    #         days_list = Helper.GetMonthDays()
    #         cursor.executemany(insert_line, ((None, day < today, day.day, day.month, day) for day in days_list))
    #         self.connection.commit()
    #         logging.info(f'Have inserted {cursor.rowcount} records to the table.')
    #
    # def get_checkboxes(self, d: Union[datetime, datetime.date], cursor: Optional[sqlite3.Cursor] = None) -> List[DataBaseCheckBox]:
    #     cursor = cursor or self.connection.cursor()
    #     days_list = cursor.execute(f"SELECT * from {self.tablename} where month = ?", (d.month, )).fetchall()
    #     return days_list
    #
    # def save_changes(self, boxes: Dict[int, QtWidgets.QCheckBox]):
    #
    #     cursor: sqlite3.Cursor = self.connection.cursor()
    #     month = datetime.now().month
    #     cursor.executemany(f'update {self.tablename} set checked = ? where day = ? and month = ?', ((box.isChecked(), index, month) for index, box in boxes.items()))
    #     self.connection.commit()
