import random
import time
from datetime import datetime, timedelta
from typing import Generator, Tuple, List, Union

USER_LIST = ['John Doe','Ivan Petrov']
ERROR_LIST = ['Error1','Error2']

InputDataType = Tuple[datetime, str, str]

def yield_error_randomly(threshold:float = 0.9):
    if random.random() > threshold:
        return (datetime.now(),'ERROR', random.choice(ERROR_LIST))

def gas_press_sometimes():

    current_action = random.choice(["PAUSE", "GAS"])

    for _ in range(random.randint(10, 20)):

        if random.random() > 0.9:
            yield (datetime.now(),current_action, True)

            e = yield_error_randomly(0.95)

            if e:
                yield(e)
            time.sleep(random.randint(3, 10))

            yield (datetime.now(),current_action, False)
            current_action = random.choice(["PAUSE", "GAS"])
            #current_status=False


def generate_data_flow_generator() -> Generator[InputDataType, None, None]:
    user: str = random.choice(USER_LIST)
    data_list = ["PROGRAM", f"USER: {user}", "TASK", "LASER"]

    for data in data_list:
        # может появляться Error
        # gas и pause могут появлятся после TASK
        # когда приходит pause true ждем pause false или error

        e = yield_error_randomly()
        if e:
            yield e
        if data == 'LASER':
            yield from gas_press_sometimes()

        yield (datetime.now(), data, True)
        time.sleep(random.randint(3, 4))

    for data in reversed(data_list):
        e = yield_error_randomly()
        if e:
            yield e
        time.sleep(random.randint(3, 5))
        yield (datetime.now(), data, False)

    #raise StopIteration
