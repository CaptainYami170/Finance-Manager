import csv

class DataHandler:
    def __init__(self, file_name='financedata.csv'):
        self.file_name = file_name

    def read_data(self):
        with open(self.file_name, mode='r') as file:
            reader = csv.reader(file)
            return list(reader)

    def write_data(self, data):
        with open(self.file_name, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)
