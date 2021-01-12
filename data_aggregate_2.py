from utils.input_data_imit import generate_data_flow_generator, InputDataType
from datetime import datetime
import logging
import pandas as pd
import sqlite3 as sq

class data_aggregate():

    def __init__(self) -> None:

        self.log = logging.getLogger(f"__main__.{__name__}")
        self.log.info(u'Начало получения данных')
        self.gen = generate_data_flow_generator()
        self.user = 'Vitaly'
        self.process_data()

    def receive_data(self) -> InputDataType:
        try:
            return next(self.gen)
        except StopIteration:
            self.gen = generate_data_flow_generator()
            return next(self.gen)

    def process_data(self) -> None:

        data_input = self.gen
        ERROR_LIST = ['Error1','Error2']

        with sq.connect('Machine_1.db'), sq.connect('Machine_2.db')  as con_1, con_2:

            cur_1 = con_1.cursor()
            cur_2 = con_2.cursor()

            for record in data_input:
                cursor.execute("insert into Artist values (Null, 'A Aagrh!') ")
