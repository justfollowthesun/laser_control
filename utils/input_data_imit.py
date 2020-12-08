import random
import datetime

from typing import Generator

USER_LIST = ['A', 'B']

def generate_data_flow() -> Generator[datetime, str, str]:

    user = random.choice(USER_LIST)

    # начало работы с прогой
    yield (datetime.now(), "START", user)

    for _ in range(10):

        yield (datetime.now(), "LASER", bool(random.randint(0, 1)))

    yield (datetime.now(), "FINISH", user)

    # raise StopIteration
