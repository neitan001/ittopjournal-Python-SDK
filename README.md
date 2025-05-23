# 🎓 ITTopJournal Python SDK

![PyPI](https://img.shields.io/pypi/v/ittopjournal)
![Python](https://img.shields.io/badge/python-3.7+-blue)

Лёгкая в использовании библиотека для взаимодействия с API журнала колледжа ITTOP  
📍 [journal.top-academy.ru](https://journal.top-academy.ru)

---

## 📚 Оглавление

- [Установка](#установка)
- [Быстрый старт](#быстрый-старт)
- [⚙️ Методы API](#-методы-api)
- [📥 Параметры](#-параметры)
- [🛠 Что такое application_key?](#-что-такое-application_key)
- [💡 Примеры](#-примеры)
- [Разработка](#разработка)
- [Лицензия](#лицензия)

---

## Установка

```bash
pip install ittopjournal
```

## Быстрый старт

```python
import ittopjournal

# Авторизация
token = ittopjournal.get_token("login", "password", "application_key")

# Получение расписания
schedule = ittopjournal.get_schedule(token, date="2025-04-21")  # Дата в формате YYYY-MM-DD
print(schedule)
```


## ⚙ Методы API

| Метод                              | Назначение                             |
|-----------------------------------|----------------------------------------|
| `get_token()`                     | Получение токена                       |
| `get_schedule()`                  | Расписание на указанную дату           |
| `get_evaluation_lessons()`        | Пары, которые нужно оценить            |
| `get_user_info()`                 | Информация о студенте                  |
| `get_feedback_info()`             | Отзывы от преподавателей               |
| `get_metric_grade_info()`         | Средний балл                           |
| `get_metric_attendance_info()`    | Процент посещаемости                   |
| `get_rating_group_info()`         | Рейтинг группы по топ-коинам           |
| `get_rating_stream_info()`        | Рейтинг потока                         |
| `get_student_visits_info()`       | Посещения и оценки                     |

## 📥 Параметры

**Авторизация:**
- `login` — логин студента из Journal
- `password` — пароль студента из Journal
- `application_key` — внутренний параметр, необходимый для получения токена

**Общие для большинства методов:**
- `token` — токен, получаемый после авторизации. Используется для доступа ко всем данным

**Специфичные параметры:**
- `date` — дата в формате `YYYY-MM-DD` (например, `2025-04-21`)  
  Используется только в методе `get_schedule()`

## 🛠 Что такое `application_key`?

`application_key` — это внутренний параметр, необходимый для получения токена при авторизации.

Чтобы получить его:

1. Откройте [journal.top-academy.ru](https://journal.top-academy.ru)
2. Нажмите `F12`, чтобы открыть инструменты разработчика
3. Перейдите на вкладку **Network**
4. Авторизуйтесь в системе
5. Найдите запрос к `/auth/login` (или похожий)
6. В теле запроса будет указан параметр `application_key` — скопируйте его и используйте в коде

> ⚠️ При изменении API ключ может стать другим — проверяйте актуальность при необходимости.

## 💡 Примеры

## Получение посещений и оценок
```python
from ittopjournal import get_token, get_student_visits_info

token = get_token(...)
grades = get_student_visits_info(token)
```

## Обработка ошибок
```python
schedule = get_schedule(token, "2025.04.21")  # ❌ Неправильный формат
if schedule is None:
    print("❗ Проверьте формат даты! Должен быть YYYY-MM-DD (например, 2025-04-21)")
```

## Разработка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/neitan001/ittopjournal-Python-SDK.git
```

2. Установите зависимости:
```bash
pip install -e .[dev]
```

## Лицензия

MIT © [Neitan Rudinsky](https://github.com/neitan001)
