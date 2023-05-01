"""
    Main rest api of this app

    In this file setups all routers for fastapi
"""


from rest_api.base_app import app
from rest_api.controllers import users
from services.constants.rest_api_prefixes import MAIN_API_PREFIX


app.include_router(users.router, 
                   prefix=MAIN_API_PREFIX)
