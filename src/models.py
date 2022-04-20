from enum import unique
from peewee import *
from .database import database

class User(Model):
    username = CharField(max_length=50, unique=True)
    edad = IntegerField(null=True)
    email = CharField(max_length=50, null=True)
    direccion = CharField(max_length=50,null=True)
    def __str__(self):
        return self.username

    class Meta:
        database = database
        table_name = 'users'    