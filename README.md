# tulsu-homework
___

## Лабораторная работа №1

1. Переходим в lab1
```shell
cd lab1
```

2. Делаем файлы first-task.py, second-task.py, third-task.py исполняемыми
```shell
chmod +x first-task.py
chmod +x second-task.py
chmod +x third-task.py
```

3. Запускаем
```shell
./first-task.py | ./second-task.py 2>>errors.txt | ./ third-task.py 2>>errors.txt
```
___

## Лабораторная работа №2

1. Переходим в lab2
```shell
cd lab2
```

2. Делаем файл second-task.py исполняемым.
```shell
chmod +x second-task.py
```

__Пример 1__

```shell
cat names_example.txt
```
```text
Alice
Zoe
michael
Liam
sofia
Th=omas
Olivia
```

```shell
./second-task.py < names_example.txt 2> error.txt
```
```text
Nice to see you Alice!
Nice to see you Zoe!
Nice to see you Liam!
Nice to see you Olivia!
```

```shell
cat error.txt
```
```text
Error: Name 'michael' needs to start uppercase!
Error: Name 'sofia' needs to start uppercase!
Error: Name 'Th=omas' contains an invalid character '='!
```

___

## Лабораторная работа №3

Минималистичная СУБД, хранящаяся в CSV.


### Установка poetry
Можно использовать любой другой инструмент для управления зависимостями и виртуальными окружениями.
```aiignore
curl -sSL https://install.python-poetry.org | python3 -
```
### Задание №1
1. В таблицу **EmployeeTable** внести индекс _department_id_.
2. Добавить функцию select для **DepartmentTable** по названию подразделения (возвращать список, т. к. таких может быть несколько)
3. Сделать проверку на то, что в каждой из таблиц присутствуют только уникальные наборы индексов по кортежам.
   То есть в таблице **EmployeeTable** не должно присутствовать ни одной записи с одинаковыми _id_ и _department_id_:
если для любых двух записей в таблице EmployeeTable _position_1_ == _position_2_ и _department_id_1_ == _department_id_2_, тогда это одни и
   те же записи (по сути условие уникального композитного индекса). Для таблицы **DepartmentTable** гарантировать, что нет двух
   записей с одинаковыми _department_id_.
4. Реализовать в **Database** классе функцию _join_, которая будет объединять таблицы по полям '_DepartmentTable.department_id_' и
'_EmployeeTable.department_id_'.
5. Написать тесты:
   1. На проверку уникальных индексов для пункта 2,
   2. Тест для проверки правильности операции **JOIN** из пункта 3.
   3. Удостовериться, что .csv файлы отсутствуют.

### Задание №2

1. Добавить третью таблицу (к примеру с товарами (Goods)), определить её аттрибуты, индексы итд.
2. Написать и оттестировать запрос, содержащий 2 JOIN операции и aggregate (AVG, MAX, MIN, COUNT).
3. Реализовать aggregate функцию.
4. Обобщить primary и unique индекс, и проверку на них - доп. балл.*

### Задание 3

1. Установите pre-commit. Напишите .pre-commit-config.yaml файл, добавьте хуки по умолчанию, которые считаете нужными.
2. Добавить хуки flake8, black, isort, pytest.
3. Добавьте проверку, что commit проходит только при покрытии кода в 100% (--cov-fail-under=100).
4. Создайте workflow в Github Actions, с задачей, которая прогоняет ваши тесты. Аналогично, добавьте проверку на покрытие кода в 100%.

### Команды
Запустить тесты с покрытием кода:
```
poetry run pytest --cov
```
