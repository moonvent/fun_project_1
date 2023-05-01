from pydantic import BaseModel, Field
from datetime import datetime
from rest_api.models.users import User


class Comment(BaseModel):
    text: str
    author: User
    time_published: datetime
    amount_likes: int = Field(0, ge=0)
