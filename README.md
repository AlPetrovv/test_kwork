# Тестовое задание для компании localcarhires.com 






## Инициализация
1. Клонирование репозитория.
   ```sh
   git clone git@github.com:AlPetrovv/test_kwork.git
   ```
2. Создание .env (вам необходимо добавить эти переменные в .env)
    ```sh
    SECRET_KEY=<your_secret_key> 
    POSTGRES_DB=<your_bd_name> 
    PGUSER=postgres # can be another
    POSTGRES_INITDB_ARGS='-A md5'
    POSTGRES_PASSWORD=<your_password>
    POSTGRES_HOST=db
    POSTGRES_PORT=5432
   ```
3. Запуск приложения
   ```sh
   docker-compose -f docker-compose.yaml up --build 
    ```

## Интерфейс

* Для начал вам нужно зайти на http://127.0.0.1:3000/
* Выбирайте действие, которое вам хотите 

