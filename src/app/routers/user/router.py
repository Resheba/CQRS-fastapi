from fastapi import APIRouter, Depends, status


router: APIRouter = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK)
async def ping():
    return "pong"
