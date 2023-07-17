from httpx import AsyncClient


TEST_RATE = 0.14
TEST_COST = 3


async def test_insurance_create(ac: AsyncClient):
    result = await ac.post(
        url='/insurance/create',
        json={
          "date": "2023-07-16",
          "cargo_type": "Glass",
          "rate": TEST_RATE
        }
    )
    bad_result = await ac.post(
        url='/insurance/create',
        json={
          "date": "2023-07-15",
          "cargo_type": "Glass",
          "rate": 'TEST_RATE'
        }
    )
    assert result.status_code == 200
    assert bad_result.status_code == 422


async def test_insurance_count(ac: AsyncClient):
    result = await ac.post(
        url='/insurance',
        json={
          "date": "2023-07-16",
          "cargo_type": "Glass",
          "cost": TEST_COST
        }
    )
    bad_result = await ac.post(
        url='/insurance',
        json={
          "date": "2023-07-15",  # not exist
          "cargo_type": "Glass",
          "cost": TEST_COST
        }
    )
    formatted_result = "{:.4f}".format(TEST_RATE * TEST_COST)

    assert result.status_code == 200
    assert result.json() == {'Insurance cost': formatted_result}
    assert bad_result.status_code == 404
