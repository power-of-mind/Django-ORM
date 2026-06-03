# 🎯 Django ORM

Учебный проект для изучения Django ORM и работы с базой данных через объектно-реляционное отображение (Object Relational Mapping).

Проект демонстрирует основные возможности Django ORM:

* создание моделей;
* выполнение CRUD-операций;
* работа с QuerySet;
* фильтрация и сортировка данных;
* связи между моделями;
* загрузка данных через fixtures;
* отображение данных в шаблонах Django.

---

## 📚 Что изучается в проекте

### Создание моделей

Django ORM позволяет описывать структуру базы данных с помощью Python-классов.

```python
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
```

После создания модели Django автоматически генерирует SQL для создания таблицы.

---

## 🔍 Основные возможности ORM

### Создание объекта

```python
Student.objects.create(
    name='John',
    age=20
)
```

### Получение данных

```python
Student.objects.all()

Student.objects.get(id=1)

Student.objects.filter(age__gte=18)
```

### Обновление данных

```python
student = Student.objects.get(id=1)
student.age = 21
student.save()
```

### Удаление данных

```python
student.delete()
```

---

## 🛠 Технологии

* Python 3
* Django
* Django ORM
* SQLite
* HTML
* CSS

---

## 🚀 Установка

### Клонирование репозитория

```bash
git clone https://github.com/power-of-mind/Django-ORM.git

cd Django-ORM
```

### Создание виртуального окружения

#### Linux / macOS

```bash
python -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Установка зависимостей

```bash
pip install -r requirements.txt
```

---

## 🔄 Миграции

Создание миграций:

```bash
python manage.py makemigrations
```

Применение миграций:

```bash
python manage.py migrate
```

Просмотр списка миграций:

```bash
python manage.py showmigrations
```

---

## 💾 Работа с Fixtures

Загрузка тестовых данных:

```bash
python manage.py loaddata data.json
```

Создание дампа базы данных:

```bash
python manage.py dumpdata > data.json
```

---

## ▶️ Запуск проекта

```bash
python manage.py runserver
```

После запуска приложение будет доступно по адресу:

```text
http://127.0.0.1:8000/
```

---

## 📁 Структура проекта

```text
Django-ORM/
│
├── app/
├── config/
├── static/
├── templates/
├── manage.py
├── requirements.txt
└── db.sqlite3
```

---

## 🧠 Полезные ORM-запросы

Получение первого объекта:

```python
Student.objects.first()
```

Получение последнего объекта:

```python
Student.objects.last()
```

Сортировка:

```python
Student.objects.order_by('name')

Student.objects.order_by('-age')
```

Подсчёт записей:

```python
Student.objects.count()
```

Проверка существования:

```python
Student.objects.filter(name='John').exists()
```

---

## 🎯 Цель проекта

Изучить основные принципы работы Django ORM:

* взаимодействие с базой данных без SQL;
* создание и изменение моделей;
* выполнение запросов через QuerySet API;
* работа со связями между объектами;
* использование миграций;
* построение CRUD-приложений на Django.

---

## 📄 Лицензия

Проект создан в образовательных целях.

---

## 👨‍💻 Автор

Power Of Mind

GitHub: https://github.com/power-of-mind
