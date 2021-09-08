# Практика
* сделать image контейнера с необходимым ПО для запуска sshd  
    [Dockerfile](Dockerfile)  
    [docker-compose.yml](docker-compose.yml)
* запустить docker-compose поднять два ssh сервера  
    ```bash
    sudo docker-compose build && sudo docker-compose up
    ```
* продемонстрировать что из одного контейнера можно войти в другой  
    * по паролю  
        * 1 -> 2  
            ![](1_to_2_pass.png)
        * 2 -> 1  
            ![](2_to_1_pass.png)
    * по ключу  
        * 1 -> 2  
            ![](1_to_2_key.png)
        * 2 -> 1  
            ![](2_to_1_key.png)
* выполнить команду  
    ![](cmd.png)
* передать файл  
    ![](scp.png)
* продемонстрировать простейший обмен данными с помощью утилиты netcat  
    ![](netcat.png)