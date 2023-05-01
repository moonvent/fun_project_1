from pydantic import BaseModel, Field

from rest_api.models.comments import Comment
from rest_api.models.users import User


class Post(BaseModel):
    text: str
    author: User
    comments: list[Comment] = Field([])
    amount_likes: int = Field(0, ge=0)

