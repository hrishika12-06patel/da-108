import csv

class FileManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        with open(self.file_path, 'r') as file:
            return file.read()

    def write_file(self, content):
        with open(self.file_path, 'w') as file:
            file.write(content)

    def append_file(self, content):
        with open(self.file_path, 'a') as file:
            file.write(content)

class CSVDataManager(FileManager):
    def __init__(self, file_path, delimiter=','):
        super().__init__(file_path)
        self.delimiter = delimiter

    def read_data(self):
        with open(self.file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file, delimiter=self.delimiter)
            return [row for row in reader]

    def write_data(self, data):
        with open(self.file_path, mode='w', newline='') as file:
            if data:
                fieldnames = data[0].keys()
                writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=self.delimiter)
                writer.writeheader()
                writer.writerows(data)

    def append_data(self, data):
        with open(self.file_path, mode='a', newline='') as file:
            if data:
                fieldnames = data[0].keys()
                writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=self.delimiter)
                if file.tell() == 0:  # Check if file is empty to write header
                    writer.writeheader()
                writer.writerows(data)

def main():
    file_path = 'sample.csv'
    
    # Initialize CSVDataManager
    csv_manager = CSVDataManager(file_path)
    
    # Write data to CSV
    data_to_write = [
        {'name': 'Priya', 'age': 22, 'city': 'Mumbai'},
        {'name': 'Bhumi', 'age': 25, 'city': 'Lucknow'}
    ]
    csv_manager.write_data(data_to_write)
    
    # Read data from CSV
    data = csv_manager.read_data()
    print("Data after writing:")
    print(data)
    
    # Append data to CSV
    data_to_append = [
        {'name': 'Rahul', 'age': 23, 'city': 'Chennai'},
        {'name': 'Dhruv', 'age': 24, 'city': 'Surat'}
    ]
    csv_manager.append_data(data_to_append)
    
    # Read data again from CSV
    data = csv_manager.read_data()
    print("Data after appending:")
    print(data)

if __name__ == "__main__":
    main()