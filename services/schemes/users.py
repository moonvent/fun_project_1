from datetime import datetime, timezone
from typing import Optional
from pydantic import BaseModel, Field


class User(BaseModel):
    _id: str = Field(..., description='ObjectId in Mongo')
    username: str
    first_name: str
    last_name: str
    registration_date: Optional[datetime] = Field(default_factory=lambda: datetime.now(tz=timezone.utc),
                                                  description='Date of user registration')

