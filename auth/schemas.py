from distutils.util import strtobool
from typing import List, Optional

from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str 
    
class TokenData(BaseModel):
    username: Optional[str]= None
    
class User(BaseModel):
    is_active: Optional[bool]= None
    
class UserInDB(User):
    hashed_password: str 