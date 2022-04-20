from pydantic import BaseModel
from typing import Optional

class UserRequestModel(BaseModel):
    username: str 
    email: Optional[str] = None
    edad: Optional[int] = None
    direccion: Optional[str] = None
class UserResponseModel(BaseModel):
    id : int 
    username : str
    email :  Optional[str] = None
    edad: Optional[int] = None
    direccion: Optional[str] = None
