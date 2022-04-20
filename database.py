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
    database="d6349dtkdlvoau",
    user="qsivylwlywidad", password="6c83829dd59dae2c383f416483e2efe40c086bd2d3f2cbd2869bf99fa463a5e1",
    host="ec2-63-32-248-14.eu-west-1.compute.amazonaws.com", port=5432

)
