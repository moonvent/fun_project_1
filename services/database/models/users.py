from services.exceptions.database.models.users import CannotCreateUser
from services.schemes.users import User
from services.database.database_init import users_collection


async def create_user_in_db(user: User):
    """
        Create user in db

        Args:
            user (User): User pydantic model
        
        Raises:
            CannotCreateUser: if can't create a new user
    """
    try:
        await users_collection.insert_one(user.dict())

    except Exception as e:
        raise CannotCreateUser(e)

