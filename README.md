## Команды docker-compose
- Запуск автотестов
```sh
docker-compose up autotests
```
- Запуск Django для демонстрации работы кода
```sh
docker-compose up runserver
```
## Примеры запросов к API

- Главная страница
```sh
0.0.0.0:8000
```
- Список страниц (Page)
```sh
0.0.0.0:8000/pages/
```
- Детальная информация о странице с pk=1 (Page)
```sh
0.0.0.0:8000/pages/1
```