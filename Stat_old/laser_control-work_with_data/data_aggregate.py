from utils.input_data_imit import generate_data_flow_generator, InputDataType
from datetime import datetime
import logging

class data_aggregate():

    def __init__(self) -> None:
        self.log = logging.getLogger(f"__main__.{__name__}")
        self.log.info(u'Начало получения данных')
        self.gen = generate_data_flow_generator()
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

        for record in data_input:

            self.log.debug(u'Получены новые данные')

            if record[1] == "PROGRAM":
                if record[2]:
                    data4user.program_start = record[0]
                else:
                    data4user.program_finish = record[0]

            if record[1] == "TASK":
                if record[2]:
                    data4user.task_start = record[0]
                else:
                    data4user.task_finish = record[0]

            if record[1] == "LASER":
                if record[2]:
                    data4user.laser_start = record[0]
                else:
                    data4user.laser_finish = record[0]

            if record[1] == "GAS":
                if record[2]:
                    data4user.gas_start = record[0]
                else:
                    data4user.gas_finish = record[0]
                    data4user.gas.append((data4user.gas_finish - data4user.gas_start).seconds)

            if record[1] == "PAUSE":
                if record[2]:
                    data4user.pause_start = record[0]
                else:
                    data4user.pause_finish = record[0]
                    data4user.laser_pause.append((data4user.pause_finish - data4user.pause_start).seconds)

            if record[1] in ERROR_LIST:
                data4user.errors[record[1]] = record[0]

    def output_data(self) -> dict:
        # = (data4user.program_finish - data4user.program_start).

        sum_time = (data4user.program_finish - data4user.program_start).seconds

        time_dict = {

        'Program_total_abs' : (data4user.program_finish - data4user.program_start).seconds,
        'Laser_total_abs' : (data4user.laser_finish - data4user.laser_start).seconds,
        'Task_total_abs' : (data4user.task_finish - data4user.task_start).seconds,
        'Pause_total_abs' : sum(data4user.laser_pause),
        'Gas_total_abs' : sum(data4user.gas),

        'Program_total_rel' : round(((data4user.program_finish - data4user.program_start).seconds/sum_time),2),
        'Laser_total_rel' : round(((data4user.laser_finish - data4user.laser_start).seconds/sum_time),2),
        'Task_total_rel' : round(((data4user.task_finish - data4user.task_start).seconds/sum_time),2),
        'Pause_total_rel' : sum(data4user.laser_pause)/sum_time,
        'Gas_total_rel' : sum(data4user.gas)/sum_time

        }

        return time_dict

class data4user():

    """
    общее время работы программы
    общее время по каждому пользователю
    время task
    время простоя
    """

    laser_pause = []
    gas = []

    user: str
    program_start: datetime
    program_finish: datetime
    task_finish: datetime
    gas_start: datetime
    gas_finish: datetime
    task_time: datetime
    pause_start: datetime
    pause_finish: datetime
    laser_start: datetime
    laser_finish: datetime
    laser_total: datetime
    errors = {}
