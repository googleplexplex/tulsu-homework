from abc import ABC, abstractmethod
import csv
import os


class SingletonMeta(type):
    """ Синглтон метакласс для Database. """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=SingletonMeta):
    """ Класс-синглтон базы данных с таблицами, хранящимися в файлах. """

    def __init__(self):
        self.tables = {}

    def register_table(self, table_name, table):
        self.tables[table_name] = table

    def insert(self, table_name, data):
        table = self.tables.get(table_name)
        if table:
            table.insert(data)
        else:
            raise ValueError(f"Table {table_name} does not exist.")

    def select(self, table_name, *args):
        table = self.tables.get(table_name)
        return table.select(*args) if table else None
    
    def load(self, table_name):
        table = self.tables.get(table_name)
        table.load()

    ### Задание 4 ###
    def join(self, left_table='employees', right_table='departments', left_attr='department_id', right_attr='id'):
        result = []
        left_data = self.tables[left_table].data
        right_data = self.tables[right_table].data
        for left_record in left_data:
            for right_record in right_data:
                if left_record[left_attr] == right_record[right_attr]:
                    right_record_clone = right_record.copy()
                    right_record_clone[left_attr] = right_record_clone.pop(right_attr)
                    merged_record = {**left_record, **right_record_clone}
                    result.append(merged_record)
                    break
        return result



class Table(ABC):
    """ Абстрактный базовый класс для таблиц с вводом/выводом файлов CSV. """

    @abstractmethod
    def insert(self, data):
        pass

    @abstractmethod
    def select(self, *args):
        pass
    
    @abstractmethod
    def load(self):
        pass


class EmployeeTable(Table):
    """ Таблица сотрудников с методами ввода-вывода из файла CSV. """
    ATTRS = ('id', 'name', 'age', 'salary', 'department_id') ### Задание 1 ###
    FILE_PATH = 'employee_table.csv'

    def __init__(self):
        self.data = []
        self.load()  # Подгружаем из CSV-файла сразу при инициализации

    def insert(self, data):
        ### Задание 3.1 ###
        entry = dict(zip(self.ATTRS, data.split()))
        same_employee = self.select(int(entry['id']), int(entry['id']))
        if (same_employee and
            any(info['department_id'] == entry['department_id'] for info in same_employee)):
            raise ValueError(f"Entry with id: {entry['id']} and department_id: {entry['department_id']} already used")
        self.data.append(entry)
        self.save()

    def select(self, start_id, end_id):
        return [entry for entry in self.data if start_id <= int(entry['id']) <= end_id]

    def save(self):
        with open(self.FILE_PATH, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.ATTRS)
            writer.writeheader()
            writer.writerows(self.data)

    def load(self):
        if os.path.exists(self.FILE_PATH):
            with open(self.FILE_PATH, 'r') as f:
                reader = csv.DictReader(f)
                self.data = [row for row in reader]
        else:
            self.data = []


class DepartmentTable(Table):
    """ Таблица подразделенией с вводом-выводом в/из CSV файла. """
    
    """ Таблица строится с автоикрементом id"""
        
    ATTRS = ('id', 'department_name')
    FILE_PATH = 'department_table.csv'

    def __init__(self):
        self.data = []
        self.load()

    ### Задание 2 ###
    def select(self, department_name):
        result = [row for row in self.data if department_name == row['department_name']]
        return result

    def get_by_id(self, start_id, end_id):
        return [entry for entry in self.data if start_id <= int(entry['id']) <= end_id]

    def insert(self, data):
        ### Задание 3.2 ###
        entry = dict(zip(self.ATTRS, data.split()))
        department_same = self.get_by_id(int(entry['id']), int(entry['id']))
        if department_same != []:
            raise ValueError(f"Id: {entry['id']} already used")
        self.data.append(entry)
        self.save()

    def save(self):
        with open(self.FILE_PATH, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.ATTRS)
            writer.writeheader()
            writer.writerows(self.data)

    def load(self):
        if os.path.exists(self.FILE_PATH):
            with open(self.FILE_PATH, 'r') as f:
                reader = csv.DictReader(f)
                self.data = [row for row in reader]
        else:
            self.data = []
