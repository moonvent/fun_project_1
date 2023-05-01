"""
    Preparing to general test
"""


import pytest, os
from motor.motor_asyncio import AsyncIOMotorClient


@pytest.fixture(scope="module")
def motor_client():
    client = AsyncIOMotorClient(os.getenv('MONGO_STRING_CONNECTION'))
    yield client
    client.close()
