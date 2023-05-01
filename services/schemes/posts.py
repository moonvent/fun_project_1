from pydantic import BaseModel, Field

from services.schemes.comments import Comment
from services.schemes.users import User


class Post(BaseModel):
    text: str
    author: User
    comments: list[Comment] = Field([])
    amount_likes: int = Field(0, ge=0)

