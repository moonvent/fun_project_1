import os
import motor.motor_asyncio

from services.constants.database import DATABASE_NAME


client = motor.motor_asyncio.AsyncIOMotorClient(os.getenv('MONGO_STRING_CONNECTION'))
db = client[DATABASE_NAME]


