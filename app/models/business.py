from .base import BaseDBModel, UUIDDBModel, CreatedUpdatedModel
from .user import DBUser
from tortoise import fields


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
