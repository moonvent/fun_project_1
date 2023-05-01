from services.exceptions.database.models.users import CannotCreateUser
from services.schemes.users import User
from services.constants.database import DbSecuence
from services.database.database_init import db


async def create_user_in_db(user: User):
    """
        Create user in db

        Args:
            user (User): User pydantic model
        
        Raises:
            CannotCreateUser: if can't create a new user
    """
    try:
        await db[DbSecuence.Users].insert_one(user.dict())

    except Exception as e:
        raise CannotCreateUser(e)

