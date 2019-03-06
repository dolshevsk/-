#  Тестовое задание wg_forge_backend (Python)
## Настройка
### 1) Postgres
Нужно подготовить базу данных Postgress на вашем компьютере, инструкции есть в самом тестовом задании. Я подключался к докеру. [докер инструкция](https://github.com/wgnet/wg_forge_backend/blob/master/docker_instructions.md).
### 2) Файлы с решенным тестовым заданием
Скачиваем из моего [репозитория](https://github.com/dolshevsk/test-work) папку flask.
### 3) virtualenv and pip
Я реализовал задание на языке python3.6, с использованием микрофреймворка flask, использоваль ОС linux.(поэтому все терминальные команды написаны под linux).
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
Скачиваем нужные пакеты. На данном этапе удобнее всего перейти в скаченную папку flask.
```
pip install -r /path/to/flask/requirements.txt
```
### 4) Скрипты
* psql.py - скрипт для 1 и 2 задания с субд
* app_test.py - unittest для приложения
* models.py - модели для субд
* app.py - собственно само приложение, 3-6 задания
### 5) Как запускать
```
python /path/to/flask/psql.py
python /path/to/flask/app.py
```
p.s. В тестовом задании 4 для того, чтобы curl запросы работали корректо, нужно url обвешивать кавычками.
например ```curl -X GET "http://localhost:8080/cats?attribute=color&order=asc&offset=5&limit=2"```.
