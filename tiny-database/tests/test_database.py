import pytest
import os
import tempfile
from database.database import Database, EmployeeTable, DepartmentTable

@pytest.fixture
def temp_employee_file():
    """ Создаем временный файл для таблицы рабочих """
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
    yield temp_file.name
    os.remove(temp_file.name)

@pytest.fixture
def temp_department_file():
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
    yield temp_file.name
    os.remove(temp_file.name)

#Пример, как используются фикстуры
@pytest.fixture
def database(temp_employee_file, temp_department_file):
    """ Данная фикстура задает БД и определяет таблицы. """
    db = Database()

    # Используем временные файлы для тестирования файлового ввода-вывода в EmployeeTable и DepartmentTable
    employee_table = EmployeeTable()
    employee_table.FILE_PATH = temp_employee_file
    department_table = DepartmentTable()
    department_table.FILE_PATH = temp_department_file

    db.register_table("employees", employee_table)
    db.register_table("departments", department_table)

    yield db


### Задание 5.i и 5.iii ###
def test_unique_departmets(database):
    database.insert("departments","1 Dep1")
    database.insert("departments","2 Dep2")
    database.insert("departments","3 Dep2")
    database.insert("departments","4 Dep3")
    database.insert("departments","5 Dep3")
    database.insert("departments","6 Dep3")
    
    dep_2_data_1 = database.select("departments", "Dep2")
    assert len(dep_2_data_1) == 2
    assert dep_2_data_1[0] == {'id': '2', 'department_name': 'Dep2'}
    assert dep_2_data_1[1] == {'id': '3', 'department_name': 'Dep2'}
    
    dep_2_data_2 = database.select("departments", "Dep3")
    assert len(dep_2_data_2) == 3
    assert dep_2_data_2[0] == {'id': '4', 'department_name': 'Dep3'}
    assert dep_2_data_2[1] == {'id': '5', 'department_name': 'Dep3'}
    assert dep_2_data_2[2] == {'id': '6', 'department_name': 'Dep3'}
    
### Задание 5.ii ###
def test_join(database):
    database.insert("employees", "1 Alice 30 70000 1")
    database.insert("employees", "2 Bob 28 60000 2")
    database.insert("employees", "3 Steve 29 100000 2")
    
    database.insert("departments","1 Dep1")
    database.insert("departments","2 Dep2")
    database.insert("departments","3 Dep3")
    
    join_data = database.join()

    assert len(join_data) == 3
    assert join_data[0] == {'id': '1', 'name': 'Alice', 'age': '30', 'salary': '70000', 'department_id': '1', 'department_name': 'Dep1'}
    assert join_data[1] == {'id': '2', 'name': 'Bob', 'age': '28', 'salary': '60000', 'department_id': '2', 'department_name': 'Dep2'}
    assert join_data[2] == {'id': '3', 'name': 'Steve', 'age': '29', 'salary': '100000', 'department_id': '2', 'department_name': 'Dep2'}
    