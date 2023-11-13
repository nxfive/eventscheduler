from .base import BaseDBModel, UUIDDBModel, CreatedUpdatedModel
from .user import DBUser
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator


class DBBusiness(BaseDBModel, UUIDDBModel, CreatedUpdatedModel):

    name = fields.CharField(50, unique=True, null=False)
    city = fields.CharField(25, null=False)
    state = fields.CharField(25, null=False)
    description = fields.CharField(250)
    owner: fields.ForeignKeyRelation[DBUser] = fields.ForeignKeyField(
        "models.DBUser", related_name="business")

    events: fields.ReverseRelation["DBEvent"]

    class Meta:
        table = "businesses"


business_pydantic = pydantic_model_creator(DBBusiness)
businessIn_pydantic = pydantic_model_creator(DBBusiness, name="BusinessIn", exclude_readonly=True)
business_pydantic_list = pydantic_queryset_creator(DBBusiness)
