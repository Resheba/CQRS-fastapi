from pydantic import BaseModel, model_validator

from src.domain.entities.user import User


class UserResponseSchema(BaseModel):
    id: str
    username: str

    @model_validator(mode='before')
    @classmethod
    def generic_username(cls, data):
        if isinstance(data, User):
            data = data.dict()
        return data
    