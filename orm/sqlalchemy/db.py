from http.client import METHOD_NOT_ALLOWED
from databases import Database
import sqlalchemy
from datetime import datetime

host="localhost"
user="root"
password=""
dbname="api_rest"
DB_URL="mysql://{user}:{password}@{host}/{dbname}".format(
    user= user,
    password= password,
    host= host,
    dbname= dbname
)

metadata= sqlalchemy.MetaData()

database= Database(DB_URL)

# creation table

register= sqlalchemy.Table(
    "register",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key= True),
    sqlalchemy.Column("name", sqlalchemy.String(512)),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime())
)

engine= sqlalchemy.create_engine(DB_URL)

# permet de creer la table 
metadata.create_all(engine)

