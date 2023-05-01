import pytest

from services.database.models.users import create_user_in_db
from services.schemes.users import User
from services.database.database_init import users_collection
from datetime import datetime, timezone, timedelta


@pytest.mark.asyncio
async def test_success_user_creation():
    """
        Success test to create a new user

        Todo:
            * Decorate this in class
            * Add a mocks
    """
    user = User(username='1',
                first_name='2',
                last_name='3')
    await create_user_in_db(user=user)
    added_user = await users_collection.find_one(sort=[("_id", -1)], limit=1)
    added_user.pop('_id')
    user = user.dict()
    added_user_date, user_date = added_user['registration_date'], user['registration_date']
    added_user['registration_date'] -= timedelta(minutes=added_user_date.minute % 1, 
                                                 seconds=added_user_date.second, 
                                                 microseconds=added_user_date.microsecond)
    user['registration_date'] -= timedelta(minutes=user_date.minute % 1, 
                                           seconds=user_date.second, 
                                           microseconds=user_date.microsecond)
    user['registration_date'] = user['registration_date'].replace(tzinfo=None)
    print(added_user, user)
    assert user == added_user

