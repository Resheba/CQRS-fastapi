from typing import Annotated
from fastapi import APIRouter, Depends, status

from src.app.core import BaseResponse, BaseHTTPException, MediatorDepend

from src.domain.entities.user import User, Username
from src.infrastructure.commands.user import CreateUserCommand, DeleteUserCommand
from src.infrastructure.queries.user import GetUserQuery
from src.infrastructure.mediator import Mediator

from .schemas import UserResponseSchema


router: APIRouter = APIRouter()


@router.get("", 
            status_code=status.HTTP_200_OK,
            response_model=BaseResponse[list[UserResponseSchema]]
            )
@BaseHTTPException.handle
async def get_users(
    mediator: Annotated[Mediator, Depends(MediatorDepend)],
):
    users, *_ = await mediator.handle_query(GetUserQuery())
    return BaseResponse(data=users)


@router.post("", 
             status_code=status.HTTP_201_CREATED,
             response_model=BaseResponse[UserResponseSchema]
             )
@BaseHTTPException.handle
async def create_user(
    mediator: Annotated[Mediator, Depends(MediatorDepend)],
    command: CreateUserCommand
):
    user, *_ = await mediator.handle_command(command)
    return BaseResponse(data=user)


@router.delete("",
               status_code=status.HTTP_204_NO_CONTENT,
               )
@BaseHTTPException.handle
async def delete_user(
    mediator: Annotated[Mediator, Depends(MediatorDepend)],
    command: DeleteUserCommand
):
    await mediator.handle_command(command)
