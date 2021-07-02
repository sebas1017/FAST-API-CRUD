from peewee import *
database = MySQLDatabase(
    database="prueba",
    user="root", password="fastapi",
    host="localhost", port=3306

)
