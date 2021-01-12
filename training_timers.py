from datetime import datetime

today = datetime.today()

date_string = '2021/01/10/10/11/23'

datetime_object = datetime.strptime(date_string, '%Y/%m/%d/%H/%M/%S')

print(datetime_object)
