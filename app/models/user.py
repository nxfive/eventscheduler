from .base import BaseDBModel, UUIDDBModel, CreatedUpdatedModel
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator


class DBUser(BaseDBModel, UUIDDBModel, CreatedUpdatedModel):

    username = fields.CharField(25, unique=True)
    email = fields.CharField(100, unique=True)
    name = fields.CharField(50)
    surname = fields.CharField(50)
    password = fields.CharField(100, null=False)
    is_active = fields.BooleanField(default=True)
    is_superuser = fields.BooleanField(default=False)
    is_verified = fields.BooleanField(default=False)
    tickets = fields.ForeignKeyField("models.DBTicket", related_name=)


    def __str__(self):
        return self.username

    class Meta:
        table = "users"

    class PydanticMeta:
        exclude = ("password",)


user_pydantic = pydantic_model_creator(DBUser)
userIn_pydantic = pydantic_model_creator(DBUser, name="UserIn", exclude_readonly=True)
userOut_pydantic = pydantic_model_creator(DBUser, name="UserOut", exclude=("password",))
user_pydantic_list = pydantic_queryset_creator(DBUser)
