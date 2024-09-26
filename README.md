# mongodb-docker
Quickly start MongoDB using Docker.

# 環境說明
- windows 11
- powershell

# 開啟步驟
1. 使用Dockerfile 建立image
image-name 的部分可以自己改
    ```
    docker build -t image-name .
    ```


2. 建一個名為data的資料夾用來掛載在container中

3. 執行container
    ```
    docker run --name container-name -d -p 27017:27017 -v $pwd\data:/data/db image-name
    ```

* 如果成功啟動container，可以在localhost:27017連到mongodb。  
        預設帳號 : mongodb  
        預設密碼 : mongodb

* 如果想更改預設帳號密碼，可以到Dockerfile中，修改以下指令等號右邊的值:  
    ```
    ENV MONGO_INITDB_ROOT_USERNAME=mongodb
    ENV MONGO_INITDB_ROOT_PASSWORD=mongodb
    ```