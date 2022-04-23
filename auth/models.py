from tortoise import fields
from tortoise.models import Model 

class User(Model):
    
    id= fields.IntField(pk= True)
    username= fields.CharField(unique= True)
    password= fields.CharField(max_length= 512) # hashed
    is_active= fields.BoolField(default= True)
    
    class PydanticMeta:
        ...