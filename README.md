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
