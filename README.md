#  Тестовое задание wg_forge_backend (Python)
## Настройка
### 1) Postgres
Нужно подготовить субд Postgress. Инструкции есть в самом тестовом задании. Я подключался к докеру. [Докер инструкция](https://github.com/wgnet/wg_forge_backend/blob/master/docker_instructions.md).
### 2) Файлы с решенным тестовым заданием
Скачиваем из моего [репозитория](https://github.com/dolshevsk/test-work) папку flask.
### 3) virtualenv and pip
Я реализовал задание на языке python3.6, с использованием микрофреймворка flask, использоваль ОС linux.(поэтому все команды для терминала написаны под linux).
Для того, чтобы скрипты работали, нужно установить язык python, настроить virtualenv, установить все нужные пакеты.
#### Установка python3.6
Смотрим на сайте python.
#### Установка virtualenv и создание изолированной среды
Перед установкой нужно обновить версию pip.
 ```pip install --upgrade pip```
Далее.
```
pip install virtualenv
virtualenv ENV
source /path/to/ENV/bin/activate
```
Скачиваем нужные пакеты. 
```
pip install -r /path/to/flask/requirements.txt
```
### 4) Скрипты
* psql.py - скрипт для 1 и 2 задания с субд
* app_test.py - unittest для приложения
* models.py - модели
* app.py - собственно само приложение, 3-6 задания
### 5) Как запускать
```
python /path/to/flask/psql.py
python /path/to/flask/app.py
```
