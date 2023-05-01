
from enum import Enum
from pydantic import BaseModel


class StatusesEnum(str, Enum):
    """
        Enum of available statuses
    """
    Success = 'success'
    Error = 'error'


class SimpleResponse(BaseModel):
    """
        Response used for simple responses, have status (str) and response (dict | str), 
        for more specified response create other

        Attributes:
            status (StatusesEnum): response status
            response_body (dict | str): any response, can be str or dict, for any other types create other response class
    """
    status: StatusesEnum
    response_body: dict | str


