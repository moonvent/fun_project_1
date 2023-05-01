from fastapi import APIRouter
from services.exceptions.database.models.users import CannotCreateUser
from services.rest_api.controllers.users.create_user import CREATE_USER_ERROR, CREATE_USER_SUCCESS
from services.schemes.responses import SimpleResponse, StatusesEnum
from services.schemes.users import User
from services.constants.rest_api_prefixes import USERS_PREFIX
from services.database.models.users import create_user_in_db


router = APIRouter(prefix=USERS_PREFIX)


@router.post('/create/')
async def create_user(user: User) -> SimpleResponse:
    try:
        await create_user_in_db(user=user)

    except CannotCreateUser as e:
        return SimpleResponse(status=StatusesEnum.Success,
                              response_body=CREATE_USER_ERROR.format(e)
                              )
    
    else:
        return SimpleResponse(status=StatusesEnum.Success,
                              response_body=CREATE_USER_SUCCESS
                              )

