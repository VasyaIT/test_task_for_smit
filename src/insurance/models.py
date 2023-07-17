from decimal import Decimal
from datetime import date

from tortoise.models import Model
from tortoise.fields import IntField, DateField, CharEnumField, DecimalField

from .enum import CargoTypes


class Insurance(Model):
    id: int = IntField(pk=True)
    date: date = DateField()
    cargo_type: CargoTypes = CharEnumField(CargoTypes)
    rate: Decimal = DecimalField(10, 4)

    class Meta:
        unique_together = (('cargo_type', 'date'),)
