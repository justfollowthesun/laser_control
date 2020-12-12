import random
import time
from datetime import datetime, timedelta
from typing import Generator, Tuple, List, Union

USER_LIST = ['John Doe','Ivan Petrov']
ERROR_LIST = ['Error1','Error2']

InputDataType = Tuple[datetime, str, str]

def generate_data_flow_generator() -> Generator[InputDataType, None, None]:
    data_list = ["PROGRAM", f"USER: {user}", "TASK", "LASER"]

    for data in data_list:
        yield (datetime.now(), data, True)
        time.sleep(random.randint(1, 3))

    for data in reversed(data_list):
        time.sleep(random.randint(1, 3))
        yield (datetime.now(), data, False)

    yield (datetime.now(), "START", user)

    bool_var = True

    for _ in range(10):

        yield (datetime.now(), "LASER", bool_var)

        bool_var = not bool_var

    yield (datetime.now(), "FINISH", user)
    raise StopIteration





def generate_data_flow() -> List[Tuple[datetime, str, Union[bool, str]]] :

    user: str = random.choice(USER_LIST)
    error: str = random.choice(ERROR_LIST)
    output_list = [[datetime.now(), 'PROGRAM', True], [datetime.now(), 'USER', user]]
    data_list = ["TASK", "LASER", "PAUSE", "GAS"]

    for data in data_list:
        i = random.randint(1, 1000)
        output_list.append([datetime.now()+timedelta(seconds=i), data, True])
        if i%7==0:
            output_list.append([datetime.now()+timedelta(seconds=random.randint(i,1000)), error, True])
        else:
            output_list.append([datetime.now()+timedelta(seconds=random.randint(i,1000)), data, False])

    output_list.append([datetime.now()+timedelta(seconds=random.randint(i,1000)), 'PROGRAM', False])
    return output_list

    # data_list = ["PROGRAM", f"USER: {user}", "TASK", "LASER"]
    #
    # for data in data_list:
    #     yield (datetime.now(), data, True)
    #     time.sleep(random.randint(1, 3))
    #
    # for data in reversed(data_list):
    #     time.sleep(random.randint(1, 3))
    #     yield (datetime.now(), data, False)
    # начало работы с прогой
    # yield (datetime.now(), "START", user)
    #
    # bool_var = True
    #
    # for _ in range(10):
    #
    #     yield (datetime.now(), "LASER", bool_var)
    #
    #     bool_var = not bool_var
    #
    # yield (datetime.now(), "FINISH", user)
    # raise StopIteration
