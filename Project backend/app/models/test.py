from mongoengine import *
from mongoengine import connect 
from datetime import datetime
from app import configs

connect(alias='db_test', db='db_test')
#connect('mydb')
class Roles(Document):
    roleName = StringField() 
    meta = {'db_alias': 'db_test'}

class Tables(Document):
    #roleId = ReferenceField()
    nama = StringField(max_length=25, required=True, unique=True)
    deskripsi = StringField(max_length=100, required=True, unique=True)
    #userEmail = EmailField(required=True, unique=True)
    #userPassword = StringField(required=True)
    #createdAt = DateTimeField(required=True, default=datetime.utcnow())
    
#def Role(Document):
    #roleName = StringField()

#def User(Document): #document itu data, collections itu tabel
    #userName = StringField()
    #userPassword = StringField()
    #role = ReferenceField(Role, null=True)
    
    meta = {'db_alias': 'db_test'}

#array = ["DOSEN", "MAHASISWA"]
#for d in array:
    #coll = Roles(rolename=d)
    #coll.save()