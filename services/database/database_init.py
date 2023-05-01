import os
import motor.motor_asyncio

from services.constants.database import DATABASE_NAME, DbSecuence


client = motor.motor_asyncio.AsyncIOMotorClient(os.getenv('MONGO_STRING_CONNECTION'))
db = client[DATABASE_NAME]

users_collection = db[DbSecuence.Users]
posts_collection = db[DbSecuence.Posts]
comments_collection = db[DbSecuence.Comments]
