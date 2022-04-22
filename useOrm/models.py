

from tortoise import fields
from tortoise.models import Model 
from tortoise.contrib.pydantic import pydantic_model_creator


class Account(Model):
    
    id= fields.IntField(pk= True)
    code= fields.BigIntField()
    name= fields.CharField(max_length=512)
    description= fields.TextField()
    
    class PydanticMeta:
        ...
        

accountOut= pydantic_model_creator(Account, name="out")
accountIn= pydantic_model_creator(Account, name="in", exclude_readonly= True)

    