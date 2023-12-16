# rock_paper_scissors
Learning project

Run on Python version: Python 3.9.6

## Setup local environment

Install `Docker` and `Docker compose` first

After installation, run the following command to create a local Docker container.

```bash
docker-compose build
docker-compose up -d
```

If Docker is running successfully, the API and DB server will be launched as shown in the following:

- API server: http://localhost:8000
- DB server: http://localhost:3306

_Be careful, it won't work if the port is occupied by another application._

If you want to check docker is actually working, then you can check it with following command:

```bash
docker ps
```

If you want to go inside of docker container, then try to use following command:

```bash
docker-compose exec mysql bash
docker-compose exec api bash
```

To shut down the docker instance, please use following command:

```bash
docker-compose down
```

### How to check the DB tables in container

You can check the DB data by actually executing a query using the following command:

```bash
docker-compose exec mysql bash
mysql -u root -p
mysql> USE fastapi_app;
mysql> SHOW TABLES;
```

Username and password can be found in the database/local.env file.

### DB Migrations

When creating DB docker container, docker will create predefined tables in `database/db` folder.
That help to control versions of database.

The main table definition has already been created with the name `game_board_table.sql`.

### Save the local DB changes as a dump file

```bash
docker-compose exec database mysqldump -u root -p fastapi_app > database/db/dump.sql
```

### API documentation
http://localhost:8000/docs#/
OR
http://localhost:8000/redoc

## Old instructions
to run the project, use the following command:
python3 -m uvicorn rock_paper_scissors.src.routes:app --reload

then there are two endpoints:
http://127.0.0.1:8000/player_1?player_id=9f466a4a-1af7-4ddf-ba6a-514b55566072&move=Rock
and 
http://127.0.0.1:8000/player_2?game_id=32119960-2e90-4e4e-9ab6-dc683c2fc653&player_id=fccd13b2-7885-43bc-918a-9700c2414315&move=Scissors