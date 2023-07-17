from decimal import Decimal
from datetime import date

from pydantic import BaseModel

from .enum import CargoTypes


class BaseInsurance(BaseModel):
    date: date
    cargo_type: CargoTypes


class InsuranceCalculate(BaseInsurance):
    cost: Decimal


class InsuranceCreate(BaseInsurance):
    rate: Decimal


class InsuranceDelete(BaseInsurance):
    pass
