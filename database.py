import os
from peewee import *
from dotenv import load_dotenv

load_dotenv()

database = os.getenv('DATABASE')
user = os.getenv('USER')
host = os.getenv('HOST')
port = os.getenv('PORT')
password = os.getenv('PASSWORD')


database = PostgresqlDatabase(
    database=database,
    user=user, password=password,
    host=host, port=5432

)
