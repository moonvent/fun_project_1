from datetime import datetime
from pydantic import BaseModel, Field


class User(BaseModel):
    _id: str = Field(..., description='ObjectId in Mongo')
    username: str
    first_name: str
    last_name: str
    registration_date: datetime

