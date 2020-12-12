from utils.input_data_imit import generate_data_flow,generate_data_flow_generator, InputDataType
from datetime import datetime

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
    #program_total: datetime = program_finish-program_start
    task_start: datetime
    task_finish: datetime
    task_time: datetime
    laser_start: datetime
    laser_finish: datetime
    laser_total: datetime
    pause_start: datetime
    pause_finish: datetime
    pause_total: datetime
    errors = {}


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

        data_list = ["TASK", "LASER", "PAUSE", "GAS"]
        ERROR_LIST = ['Error1','Error2']

        a=generate_data_flow()

        for x in a:
            print(x)

        data4user.user = a[1][2]

        for record in a:
            print(record)
            if record[1]=="PROGRAM":
                if record[2]:
                    data4user.program_start=record[0]
                else:
                    data4user.program_finish=record[0]

            if record[1]=="TASK":
                if record[2]:
                    data4user.task_start=record[0]
                else:
                    data4user.task_finish=record[0]

            if record[1]=="LASER":
                if record[2]:
                    data4user.laser_start=record[0]
                else:
                    data4user.laser_finish=record[0]

            if record[1]=="PAUSE":
                if record[2]:
                    data4user.pause_start=record[0]
                else:
                    data4user.pause_finish=record[0]

            if record[1] in ERROR_LIST:
                data4user.errors[record[1]]=record[0]
            return(data4user)

data_simulate=data_aggregate()
data_simulate.process_data()

user1=data4user()
#print(user1.task_start)
