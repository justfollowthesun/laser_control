
import os
import logging
import sqlite3
# import pandas as pd
from config import DB_PATH, DB_DIR


class Database():

    tablename: str = 'authorization'
    connection = None

    def __init__(self) -> None:

        if not os.path.exists(DB_DIR):
            os.mkdir(DB_DIR)

        self.connection = sqlite3.connect(DB_PATH)
        logging.info("Successfully connect to database")
        self.create_table()
        self.create_testing_login()
        # self.put_login_password_to_db()
        logging.info("Successfully load environment")

    def authorization_check(self, login:str, password:str) -> bool:

        cursor: sqlite3.cursor = self.connection.cursor()
        result = cursor.execute(f"select login, password from {self.tablename} where login = ? and password = ? ",(login,password))
        return bool(cursor.fetchone())

    def add_new_user(self, login:str, password:str)->None:

        cursor: sqlite3.cursor = self.connection.cursor()
        insert_line = f'insert into {self.tablename} (login, password, is_master, is_authorized) values(?, ?, ?, ?)'
        cursor.execute(insert_line, (login, password, False, False))
        self.connection.commit()
        logging.info(f'Have inserted {cursor.rowcount} records to the table.')

    def close(self) -> None:
        
        if self.connection:
            self.connection.close()
            logging.info("Database connection was closed")

    def create_table(self) -> None:

        """
        Create table with name self.tablename in selected database
        """

        cursor:sqlite3.cursor = self.connection.cursor()
        cursor.execute(f'drop table {self.tablename} ')

        # Есть один мастер-аккаунт, который пользователь создаёт при
        # первом запуске программы.
        # Мастер аккаунт может быть создан лишь единожды

        cursor.execute(f"""create table if not exists {self.tablename}
        (
            id integer primary key AUTOINCREMENT,
            login string,
            password string,
            is_master bool,
            is_authorized bool
        )""")


    def create_testing_login(self):
        cursor: sqlite3.cursor = self.connection.cursor()
        insert_line = f'insert or ignore into {self.tablename} (login, password, is_master, is_authorized) values(?, ?, ?, ?)'
        cursor.execute(insert_line, ('login', 'password', False, False))
        self.connection.commit()
        logging.info(f'Have inserted {cursor.rowcount} records to the table.')

    # def put_login_password_to_db(self):
    #     cursor: sqlite3.cursor = self.connection.cursor()
    #     keys=pd.read_excel('Keys.xlsx', names=['Name','Login','Password', 'Master'])
    #     for i in range(0, keys.shape[0]):
    #         insert_line = f'insert into {self.tablename} (login, password, is_master, is_authorized) values(?, ?, ?, ?)'
    #         cursor.execute(insert_line, (str(keys.Login[i]), str(keys.Password[i]), bool(keys.Master[i]), True))
    #     self.connection.commit()
    #     logging.info(f'Have inserted {cursor.rowcount} records to the table.')

    def signup_check(self, login:str) -> bool:
        cursor: sqlite3.cursor = self.connection.cursor()
        result = cursor.execute(f"select login from {self.tablename} where login = ? ",(login,))
        return bool(cursor.fetchone())

    def check_if_master_exists(self) -> bool:
        cursor: sqlite3.cursor = self.connection.cursor()
        result = cursor.execute(f"select count(*) from {self.tablename} where is_master = true")
        return bool(cursor.fetchone())

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
