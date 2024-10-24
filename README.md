# Инструкция по запуску проекта

>[!NOTE]
>Версия языка программирования Python должна быть 3.9.x и все последующие действия будут для Windows

1. Создаете папку с названием проекта (например geodjango)
2. Открываете эту папку в терминале:
Сначало нажимаете на клавищи Win+R, затем указываете путь к проекту через команду cd
Например:
```bash
cd C:\geodjango
```
3. Создаем виртуальную среду:
```bash
pip install virtualenv
python -m venv venv
```
4. Запускаем виртуальную среду:
```bash
venv\Scripts\activate
```
5. Теперь устанавливаем нужные библиотеки:
Сначало скачайте библиотеку [gdal](https://github.com/ilyaognev69/AlyansIT/releases/download/GDAL/GDAL-3.9.2-cp39-cp39-win_amd64.whl) (почему-то gdal от самого django работает не корректно)

Заодно и [это](https://download.osgeo.org/osgeo4w/v2/osgeo4w-setup.exe) (оно пригодится в дальнейшем). Как скачаете сразу установите на диск C (то есть чтобы в диске C находились все файлы, т.к. в settings.py указан путь именно через диск C)
```bash
pip install <путь к скачанной библиотеке>
pip install psycopg2-binary
pip install Django
pip install djangorestframework
```
6. Скачиваем PostgreSQL и создаем новую БД:
Скачиваем PostgrSQL и устанваливаем. Затем в StackBuilder доустанавливаем Postgis

Открываем SQLShell и вводим следующие команды
```bash
CREATE USER geodjango WITH PASSWORD '12345';
CREATE DATABASE geodjango OWNER geodjango ENCODING 'UTF8';
ALTER USER geodjango WITH SUPERUSER;
CREATE EXTENSION postgis;
```
7. И последнее:
Просто все файлы из github перекидываем в проект и запускаем
```bash
cd AlyansIT
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Запрсы через api находятся по ссылке http://localhost:8000/api/polygons/
А просмотр конкретного полигона по ссылке http://localhost:8000/api/polygons/{id}/
