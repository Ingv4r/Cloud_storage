from fastapi.responses import HTMLResponse
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Request
from fastapi.templating import Jinja2Templates

from database import get_async_session
from auth.models import User, user
from .schemas import UserRead

from auth.base_config import current_user


router = APIRouter(prefix="/users", tags=["Users"])
templates = Jinja2Templates(directory="../templates")


@router.get('/', response_class=HTMLResponse, response_model=list[UserRead])
async def get_users_list(request: Request, session: AsyncSession = Depends(get_async_session)):
    query = select(user)
    result = await session.execute(query)
    return templates.TemplateResponse(
        "item.html",
        {"request": request, "users": result.all()}
    )

