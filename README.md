# FastAPI Q&A Service

Простой сервис для работы с вопросами и ответами на FastAPI + PostgreSQL в Docker.

---

## 1. Настройка окружения
Создайте файл `.env` на основании шаблона `.env.template`:

```env
# Юзер БД с полными правами (для миграций)
POSTGRES_USER=<your_username>
POSTGRES_PASSWORD=<your_password>
POSTGRES_DB=<database_name>

# Юзер БД с ограниченными правами (не создается автоматически, можно не указывать)
APP_DB_USER=<your_username>
APP_DB_PASSWORD=<your_password>

# Окружение
ENV=dev  # влияет на доступность документации (dev/prod)
```
## 2. Запуск проекта

Запуск базы данных:
```
docker-compose up -d db
```

Запуск веб-приложения:
```
docker-compose up -d web
```
## 3. Документация API
Если ENV=dev, документация будет доступна по адресу:
```
http://localhost:8000/docs
```
## 4. API
Вопросы:
```
GET /api/v1/questions/  -  Получить список всех вопросов
POST /api/v1/questions/  -  Создать новый вопрос
GET /api/v1/questions/{id}  -  Получить вопрос и все ответы на него
DELETE /api/v1/questions/{id}  -  Удалить вопрос вместе с ответами
```
Ответы:
```
POST /api/v1/questions/{id}/answers/  -  Добавить ответ к вопросу
GET /api/v1/answers/{id}  -  Получить конкретный ответ
DELETE /api/v1/answers/{id}  -  Удалить ответ
```



