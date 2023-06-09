# Тестовое задание для компании localcarhires.com 






## Инициализация
1. Клонирование репозитория.
   ```sh
   git clone git@github.com:AlPetrovv/test_dadata.git
   ```
   
2. Активация виртуального окружения.
   ```sh
   cd test_dadata
   python3.10 -m venv venv
   source venv/bin/activate если linux .\venv\Scripts\activate если Windows
    ```
    
3. Скачивание зависимоcтей.
    ```sh
   (venv) $ pip install -r requirements.txt
   ```
   
## Запуск
 ```sh
   python3 app/manage.py
  ```
## Интерфейс

* Для начал вам нужно ввести токен для сервиса dadata
* Выбрать язык (ru/en)
* Следовать инструкциям для выполнения определенных действий 

## Ошибки

* Если у что-то не получилось или вы получили ошибку, нужно заново запустить скрипт(см. Запуск)

## Подсказки
* Если у ва произошла ошибка при соединении на сервер 403 Error, попробуйте обновить свой token(API-ключ) в личном кабинете dadata

## Видеоподсказка
  
<a href="https://asciinema.org/a/568193" target="_blank"><img src="https://asciinema.org/a/568193.svg" /></a>