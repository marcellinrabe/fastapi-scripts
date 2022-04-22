from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator

class ToDo(models.Model):
    id = fields.IntField(pk=True)
    toDo = fields.CharField(max_length=255)
    due_date = fields.CharField(max_length=255)

    class PydanticMeta:
        ...
    

toDoPydantic = pydantic_model_creator(ToDo, name="to do pydantic")
toDoIn = pydantic_model_creator(ToDo, name="to do in", exclude_readonly=True)