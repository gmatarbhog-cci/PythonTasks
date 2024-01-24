import ast
import time
from DBUtils import DBUtils

class MeasureTime:
    def __init__(self):
        self.db = DBUtils()
        self.db.create_table()
    all_entries = []

    def track_time(self, value, type, source):
        self.all_entries.append({'func': source, 'type': type, 'value': value})
        self.save_time_log([(type, source, value)])

    def show_message(self):
        self.track_time(time.time(), 'start', 'show_message')
        print('Running some code here')
        time.sleep(1)
        self.track_time(time.time(), 'end', 'show_message')

    def print_message(self):
        self.track_time(time.time(), 'start', 'print_message')
        print('Running some code here')
        time.sleep(1)
        self.track_time(time.time(), 'end', 'print_message')

    def log_time_entries(self):
        # call function 3 times to simulate storing of time entries
        for i in range(2):
            self.show_message()
            self.print_message()
        # write logs to file
        try:
            with open("time-log.txt", "w") as file:
                file.write(str(self.all_entries))
                file.close()
                print('Time logs written to file')
        except Exception as error:
            print(error)

    def find_log_entries(self, source):
        # opening the file in read mode
        log_data = open("time-log.txt", "r").read()

        for log in ast.literal_eval(log_data):
            if log['func'] == source:
                print(log)

    def save_time_log(self, data):
        result = self.db.insert_data(data)
        print('Inserted {} record.'.format(result))


measure_time = MeasureTime()
measure_time.log_time_entries()
measure_time.find_log_entries('show_message')
# measure_time.db.truncate_data()