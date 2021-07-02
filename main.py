from typing import Optional
from fastapi import FastAPI
from peewee import OperationalError
from fastapi import FastAPI
from database import database as connection
from models import User
from fastapi import HTTPException


from schemas  import (UserRequestModel, UserResponseModel)
app = FastAPI(title="API REST DINAMICA",
              description="Registro de Usuarios",
              version='1.0.1')
@app.on_event("startup")
async def startup():
    if connection.is_closed():
        connection.connect()
    
@app.on_event("shutdown")
async def shutdown():
    if not connection.is_closed():
        connection.close()
@app.get("/")
async def index():
    return "Bienvenido a esta sencilla APIREST para el registro de usuarios en MYSQL"

@app.get("/about")
async def about():
    return "Desarrollado por: Sebastian Henao Erazo"


@app.post("/users")
async def create_user(user_request: UserRequestModel):
    try:
        validate = User.select().where(User.username == user_request.username).first()
        if validate:
            return "Error este usuario ya existe lo sentimos intente nuevamente con un nombre distinto"    
        user = User.create(
            username = user_request.username,
            email = user_request.email,
            direccion= user_request.direccion,
            edad= user_request.edad,
            )       
        return (user,"creado correctamente")
    except OperationalError:
        return "Por el momento nuestro servidor se encuentra abajo Espere por favor..."


@app.get("/users/{user_id}")
async def get_user(user_id):
    user = User.select().where(User.id == user_id).first()
    if user:
        return (UserResponseModel(
                id = user.id , 
                username = user.username, 
                email = user.email,
                edad = user.edad,
                direccion = user.direccion,
                ),"status:Consulta Realizada correctamente")          
    else:
        return HTTPException(404,'Usuario no encontrado')


@app.delete("/users/{user_id}")
async def delete_user(user_id):
    try:
        user = User.get(User.id == user_id)
        user.delete_instance()
        return "Usuario Eliminado Correctamente"
    except Exception as ex:
        print(ex)
        return f"El usuario con id {user_id} no existe en nuestro sistema"  

  
@app.put("/updateUser/{user_id}")
def update_user(user_id,username,direccion:Optional[str]= None,
             email:Optional[int]= None, edad:Optional[int]= None):
    user = User.get(User.id == user_id)
    if not user:
        return f"Error el usuario con id {user_id} no existe"
    try:        
        User.update(username=username,
                direccion=direccion if direccion !=None and direccion.replace(" ","")!= "" else user.direccion,
                email=email if email !=None and email.replace(" ","")!= "" else user.email,
                edad=edad if edad !=None and edad!= "" else user.edad,
                    ).where(User.id== user_id).execute()
        return "Registro actualizado correctamente"
    except OperationalError:
        return "Lo sentimos presentamos errores en nuestro servidor favor intente mas tarde"    
        


@app.get("/allUsers/")
def get_all_users():
    users = list(User.select().dicts())
    return users if len(users) > 0 else  "No existen registros para esta consulta"