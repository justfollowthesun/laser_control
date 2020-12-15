from utils.input_data_imit import generate_data_flow_generator, InputDataType
from datetime import datetime

class data_aggregate():

    def __init__(self) -> None:
        # self.data = self.data_processing()
        self.gen = generate_data_flow_generator()


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
            print(record)
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

            if record[1] == "PAUSE":
                if record[2]:
                    data4user.pause_start = record[0]
                else:
                    data4user.pause_finish = record[0]

            if record[1] in ERROR_LIST:
                data4user.errors[record[1]] = record[0]
        return(data4user)

class data4user():

    """
    общее время работы программы
    общее время по каждому пользователю
    время task
    время простоя
    """

    user: str
    program_start: datetime
    program_finish: datetime
    task_finish: datetime
    task_time: datetime
    laser_start: datetime
    laser_finish: datetime
    laser_total: datetime
    pause_start: datetime
    pause_finish: datetime
    pause_total: datetime
    errors = {}

class data_forming():
    pass

a = data_aggregate()
print(a.process_data())

gen = generate_data_flow_generator()

# for data in gen:
#     print(data)
