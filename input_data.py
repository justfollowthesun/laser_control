import random
import time
from datetime import datetime, timedelta
from typing import Generator, Tuple, List, Union


# input data structure is [date ov event, user_id, machine_id, operation name, status]

list_of_events = [
    ["2021-02-02 09:00:00", 'User_2', 'Machine_1', 'PROGRAM', 'START'],
    ["2020-12-01 10:05:00", 'User_1', 'Machine_1', 'TASK', 'START'],
    ["2020-12-01 10:05:00", 'User_1', 'Machine_1', 'LASER', 'START'],
    ["2020-12-01 10:05:30", 'User_2', 'Machine_1', 'GAS', 'START'],
    ["2020-12-01 10:06:30", 'User_2', 'Machine_1', 'GAS', 'FINISH'],
    ["2020-12-01 10:07:00", 'User_1', 'Machine_1',  'LASER', 'FINISH'],
    ["2020-12-01 10:07:30", 'User_1', 'Machine_1', 'ERROR_1', 'FINISH'],
    ["2020-12-01 10:09:00", 'User_1', 'Machine_1',  'TASK', 'FINISH'],
    ["2020-12-01 10:30:00", 'User_1', 'Machine_1', 'PROGRAM', 'FINISH']
        ]


def data_generator():

    for event in list_of_events:

        yield event

def data_generate():

    try:

        return next(data_generator())
    except StopIteration:

        data_generator()
        return next(data_generator())

gen = data_generator()

# try:
#     print(next(gen_data))
# except StopIteration:
#     gen_data = test_generator.generate_data_flow()
#     print(next(gen_data))


# class InputData_2(): #overall input data without generation structure
#
#     def __init__(self):
#
#         self.data = [
#
#             ["2020-12-01 10:00:00", 'User_1', 'Machine_1', 'PROGRAM', 1],
#
#             ["2020-12-01 10:05:00", 'TASK', 1],
#             ["2020-12-01 10:05:00", 'LASER', 1],
#             ["2020-12-01 10:05:30", 'GAS', 1],
#             ["2020-12-01 10:06:30", 'GAS', 1],
#             ["2020-12-01 10:07:00", 'LASER', 0],
#             ["2020-12-01 10:07:30", 'ERROR_1', 0],
#             ["2020-12-01 10:09:00", 'TASK', 0],
#             ["2020-12-01 10:30:00", 'PROGRAM', 0]
#
#         ]
#         self.user_login = 'User_1'
#         self.machine = 'Machine_1'
