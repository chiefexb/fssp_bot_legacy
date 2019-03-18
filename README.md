# FSSP_BOT - бот для мессежеров взаимодействует с API ФССП РФ

## Введение
Бот создан Алексеем Шило. Я работал ранее в Федеральной службе судебных приставов `УФССП РФ`. 
Этот бот использует `Open API` умеет работать с мессенжером Telegram.
В планах VK, Viber,  Facebook
## Установка

## Настройка БД
```
psql -U postgres -h localhost
CREATE DATABASE fsspbot;
CREATE USER fsspbot WITH PASSWORD 'fssp_pass';
GRANT ALL PRIVILEGES ON DATABASE fsspbot TO fsspbot;
```
 
