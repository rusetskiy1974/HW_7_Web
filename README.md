DZ_7_WEB


docker run --name some-postgress -p 5432:5432 -e POSTGRES_PASSWORD=12345 -d postgres


DBeaver create  postgress base with password 12345


DBeaver create new postgress base with name HW_7


alembic revision --autogenerate -m 'Init'  


alembic upgrade head   


py main.py






