from decimal import Decimal
from typing import List

from .models import Insurance
from .schemas import InsuranceCalculate, InsuranceCreate, InsuranceDelete


async def insurance_calculate(data: InsuranceCalculate) -> Decimal:
    insurance = await Insurance.get(date=data.date, cargo_type=data.cargo_type.value)
    return insurance.rate * data.cost


async def create_insurance(data: InsuranceCreate) -> Insurance:
    return await Insurance.create(**data.model_dump())


async def delete_insurance(data: InsuranceDelete) -> 0 | 1:
    return await Insurance.filter(**data.model_dump()).delete()


async def all_insurance() -> List[Insurance]:
    return await Insurance.all()
