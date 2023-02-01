Анфиса - погодный ассистент - "мороженщик"
=====

Описание проекта:
----------
Проект создан в качестве учебного курса

Погодный ассистент узнает погоду в нужном городе и, в зависимости от нее, советует мороженое


Стек технологий:
----------
* Python
* Django
* HTML


Установка проекта из репозитория:
----------

1. Клонировать репозиторий и перейти в него в командной строке:
```bash
git clone https://github.com/NazLun/Anfisa_yandex
cd anfisa
```
2. Cоздать и активировать виртуальное окружение:
```bash
python3 -m venv venv
source venv/bin/activate
```
3. Установить зависимости из файла ```requirements.txt```:
```bash
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```
5. Запустить проект (в режиме сервера Django):
```bash
python3 manage.py runserver
```
