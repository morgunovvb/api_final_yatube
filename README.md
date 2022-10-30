# api_final
api final

Описание проекта:
Это проект API для Django-проекта Yatube. С помощью апи можно универсальный доступ на разные устройства предоставлять. А также устанавливать и проверять различные уровни доступа для разных пользователей.
_______


Инструкция по запуску.

Клонировать репозиторий и перейти в него в командной строке:
https://github.com/morgunovvb/api_final_yatube

Перейти в созданную директорию:
cd api_final_yatube

Cоздать виртуальное окружение:
python3 -m venv venv

Активировать виртуальное окружение:
source venv/bin/activate

Установить зависимости из файла requirements.txt:
pip install -r requirements.txt

Сделать миграции:
python3 manage.py makemigrations

Применить миграции:
python3 manage.py migrate

Поднять сервер:
python3 manage.py runserver
_______



Пример POST-запроса с токеном Антона Чехова: 
добавление нового поста.
POST .../api/v1/posts/

Пример ответа:
{
    "text": "Вечером собрались в редакции «Русской мысли»,
    чтобы поговорить о народном театре. Проект Шехтеля всем нравится.",
    "group": 1
}

Пример GET-запроса:
получаем информацию о группе.
GET .../api/v1/groups/2/

Пример ответа:
{
    "id": 2,
    "title": "Математика",
    "slug": "math",
    "description": "Посты на тему математики"
} 

Использованные технологии:
Django==4.1.2
pytest==6.2.4
pytest-pythonpath==0.7.3
pytest-django==4.4.0
djangorestframework==3.12.4
djangorestframework-simplejwt==4.7.2
Pillow==9.3.0
PyJWT==2.1.0
requests==2.26.0
djoser==2.1.0
pytz==2022.5
db.sqlite3



об авторе: https://github.com/morgunovvb
