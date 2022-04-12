# initiations à l'utilisation de l'ORM tortoise de python


#
#    fields signifie champs. 
#    un champ signifie donc une colonne dans la base des données 
#    donc fields créer une colonne dans la base des données
#    Et models c'est le modèle, c'est à dire la classe qui va
#    interagir avec la base de données

from unittest.util import _MAX_LENGTH
from tortoise import fields, models

#
#    pytandic_model_creator va donc créer une classe comme 
#    BaseModel 

from tortoise.contrib.pydantic import pydantic_model_creator


class ToDo(models.Model):

    id = fields.IntField(pk=True)
    todo = fields.CharField(max_length=250)
    due_date = fields.CharField(max_length=250)

    class PydanticMeta:
        ...

ToDo_Pydantic = pydantic_model_creator(ToDo, name="Todo")

ToDoIn_Pydantic = pydantic_model_creator(ToDo, name="ToDoIn", exlude_readonly=True)

