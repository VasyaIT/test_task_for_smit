from decimal import Decimal
from typing import Dict, List

from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_400_BAD_REQUEST

from .schemas import InsuranceCalculate, InsuranceCreate, InsuranceDelete
from .services import insurance_calculate, create_insurance, delete_insurance, all_insurance

insurance_router = APIRouter(prefix='/insurance', tags=['Insurance'])


@insurance_router.post('', name='Calculate')
async def insurance_count(data: InsuranceCalculate) -> Dict[str, Decimal]:
    insurance_cost = await insurance_calculate(data)
    return {'Insurance cost': insurance_cost}


@insurance_router.post('/create', name='Create', response_model=InsuranceCreate)
async def insurance_create(data: InsuranceCreate):
    return await create_insurance(data)


@insurance_router.delete('/delete', name='Delete')
async def insurance_delete(data: InsuranceDelete) -> Dict[str, str]:
    if not await delete_insurance(data):
        raise HTTPException(HTTP_400_BAD_REQUEST, 'Insurance not found')
    return {'success': 'insurance deleted successfully'}


@insurance_router.get('/all', name='All', response_model=List[InsuranceCreate])
async def insurance_list():
    return await all_insurance()
