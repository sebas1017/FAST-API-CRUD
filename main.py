from modulefinder import ReplacePackage
from typing import Optional
from fastapi import FastAPI, Response
from peewee import OperationalError
from fastapi import FastAPI
from database import database as connection
from models import User
from fastapi import HTTPException


from schemas  import (UserRequestModel, UserResponseModel)
app = FastAPI(title="API REST DINAMICA",
              description="Registro de Usuarios",
              version='1.0.1')

def run_migrations():
    try:
        connection.create_tables([User])
        print("proceso de creacion de tablas ejecutado exitosamente")
    except Exception as e:
        print(e)



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
    return "Bienvenido a esta sencilla API-REST para el registro de usuarios en PostgreSQL"

@app.get("/api/about")
async def about():
    return "Desarrollado por: Sebastian Henao Erazo"


@app.post("/api/users", status_code=201)
async def create_user(user_request: UserRequestModel,response: Response):
    try:
        validate = User.select().where(User.username == user_request.username).first()
        if validate:
            response.status_code = 400
            return "Error este usuario ya existe lo sentimos intente nuevamente con un nombre distinto"    
        user = User.create(
            username = user_request.username,
            email = user_request.email,
            direccion= user_request.direccion,
            edad= user_request.edad,
            )       
        return (user,"creado correctamente")
    except OperationalError:
        response.status_code = 500
        return "Por el momento nuestro servidor se encuentra abajo Espere por favor..."


@app.get("/api/users/{user_id}")
async def get_user(user_id, response:Response):
    user = User.select().where(User.id == user_id).first()
    if user:
        response.status_code = 200  
        return (UserResponseModel(
                id = user.id , 
                username = user.username, 
                email = user.email,
                edad = user.edad,
                direccion = user.direccion,
                ),"status:Consulta Realizada correctamente")        
    else:
        response.status_code = 404
        return 'Usuario no encontrado'


@app.delete("/api/users/{user_id}")
async def delete_user(user_id, response:Response):
    try:
        user = User.get(User.id == user_id)
        user.delete_instance()
        response.status_code = 204
        return "Usuario Eliminado Correctamente"
    except User.DoesNotExist:
        response.status_code = 404
        return f"El usuario con id {user_id} no existe en nuestro sistema"
    except :
        response.status_code = 500
        return "Por el momento nuestro servidor se encuentra abajo Espere por favor..."

  
@app.put("/api/users/{user_id}")
async def update_user(response:Response,user_id,username,direccion:Optional[str]= None,
             email:Optional[int]= None, edad:Optional[int]= None):    
    try:
        user = User.get(User.id == user_id)
        User.update(username=username,
                direccion=direccion if direccion !=None and direccion.replace(" ","")!= "" else user.direccion,
                email=email if email !=None and email.replace(" ","")!= "" else user.email,
                edad=edad if edad !=None and edad!= "" else user.edad,
                    ).where(User.id== user_id).execute()
        response.status_code = 204
        return "Registro actualizado correctamente"

    except User.DoesNotExist:   
        response.status_code = 404
        return f"Error el usuario con id {user_id} no existe"      
    except OperationalError:
        response.status_code = 500
        return "Lo sentimos presentamos errores en nuestro servidor favor intente mas tarde"    
        


@app.get("/api/users")
def get_all_users(response:Response):
    try:
        response.status_code = 200
        users = list(User.select().dicts())
        return users if len(users) > 0 else  "No existen registros actualmente en la base de datos"
    except Exception as e:
        response.status_code = 500
        "Lo sentimos presentamos errores en nuestro servidor favor intente mas tarde"    


if __name__=="__main__":
    run_migrations()