import logger
import random
import datetime

for log in range(200):
    # new_log = logger.Log(f'LogNum - {random.randint(0,10)}', datetime.datetime(random.randint(2020,2022, random.randint(1,12), random.randint(1,25))))
    new_log = logger.Log(f'LogNum - {random.randint(1, 10)}', datetime.datetime(random.randint(2021, 2022), random.randint(1, 12), random.randint(1, 25)))
    new_log.write_log()

print(logger.Log.get_all_logs())
print(logger.Log.get_last_event())
print(logger.Log.get_logs())

