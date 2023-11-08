from tortoise.models import Model
from tortoise import fields


class BaseDBModel(Model):
    id = fields.BigIntField(pk=True, index=True)

    class Meta:
        abstract = True


class CreatedUpdatedModel:
    created_at = fields.DatetimeField(null=True, auto_now_add=True)
    updated_at = fields.DatetimeField(null=True, auto_now=True)


class UUIDDBModel:
    hash_id = fields.UUIDField(unique=True, pk=False)