from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.menu_category_schema import CategoryCreate
from app.schemas.menu_item_schema import MenuItemCreate, MenuItemUpdate
from app.dependencies.auth_dependency import get_current_user
from app.controllers import menu_controller

router = APIRouter()

@router