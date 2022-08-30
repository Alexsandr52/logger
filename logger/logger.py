from cgi import test
import datetime
import os
import shutil
import sattings
now = datetime.datetime.now()


class Log:
    last_event = None
    path = None
    def __init__(self, log, date, path=None) -> None:
        self.log = log
        if type(date) == type(datetime.datetime(1,1,1)) and date > datetime.datetime(2020,1,1):
            self.date = date
        else:
            raise ValueError('Date wrong', date)
        if path != None and os.path.exists(path):
            Log.path = path
        elif Log.path == None and not os.path.exists(sattings.default_path):
            Log.path = sattings.default_path
            os.mkdir(Log.path)
        elif Log.path == None and os.path.exists(sattings.default_path):
            Log.path = sattings.default_path
        
        Log.last_event = f'[{self.date.strftime(sattings.data_format)}] {self.log}'

    def write_log(self) -> None:

        file_path = f'log_{self.date.strftime(sattings.data_format)}'
        try:
            with open(f'{Log.path}/{file_path}', 'r+', encoding='UTF-8') as f:
                check = f'[{self.date.strftime(sattings.data_format)}] {self.log}{sattings.log_sep}'
                if check not in f:
                    f.writelines(f'[{self.date.strftime(sattings.data_format)}] {self.log}{sattings.log_sep}')
        except:
            with open(f'{Log.path}/{file_path}', 'w', encoding='UTF-8') as f:
                f.writelines(f'[{self.date.strftime(sattings.data_format)}] {self.log}{sattings.log_sep}')
    
    @staticmethod
    def clear_log() -> None:
        file_path = f'log_{now.strftime(sattings.data_format)}'
        try:
            os.remove(f'{Log.path}/{file_path}')
        except:
            print(f'To day no logs ...')

    @staticmethod
    def get_logs() -> list:
        file_path = f'log_{now.strftime(sattings.data_format)}'
        log_list = list()
        try:
            with open(f'{Log.path}/{file_path}', 'r', encoding='UTF-8') as f:
                for log in f:
                    log = log.split()
                    log_list.append((log[0], ' '.join(log[1:])))
            return log_list
        except:
            print(f'To day no logs ...')
            return log_list

    @staticmethod
    def get_last_event() -> str:
        if Log.last_event == None:
            return 'no events yet'
        return Log.last_event
    
    @staticmethod
    def get_all_logs() -> list:
        name = 'log_'
        file_list = list()
        for root, dirs, files in os.walk(Log.path):
            for file in files:
                if name in file:
                    file_list.append(file)
        return file_list

    @staticmethod
    def clear_all_logs() -> None:
        if input('clear all logs Y/n: ').lower() == 'y':
            shutil.rmtree(Log.path)

if __name__ == '__main__':
    test = Log('test1', datetime.datetime(2022, 1, 1))
    test1 = Log('test2', datetime.datetime(2022, 1, 1))
    test.write_log()
    test1.write_log()

    test3 = Log('test3', datetime.datetime(2022, 8, 31))
    test4 = Log('test4', datetime.datetime(2022, 8, 31))

    test3.write_log()
    test4.write_log()

    print(Log.get_logs())

    # Log.clear_log()
    # Log.clear_all_logs()