from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.menu_category_schema import CategoryCreate
from app.schemas.menu_item_schema import MenuItemCreate, MenuItemUpdate
from app.dependencies.auth_dependency import get_current_user
from app.controllers import menu_controller

router = APIRouter()

@router.get("/menu-categories")
def get_categories(db: Session = Depends(get_db), user = Depends(get_current_user)):
    return menu_controller.get_categories(db)

@router.post("/menu-categories")
def create_category(data: CategoryCreate, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return menu_controller.create_category(data, db)

@router.put("/menu-categories/{id}")
def update_category(id: int, data: CategoryCreate, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return menu_controller.update_category(id, data, db)


@router.delete("/menu-categories/{id}")
def delete_category(id: int, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return menu_controller.delete_category(id, db)



#------------menu items-----------------
@router.get("/menu-items")
def get_items(db: Session = Depends(get_db), user = Depends(get_current_user)):
    return menu_controller.get_items(db)


@router.post("/menu-items")
def create_item(data = MenuItemCreate, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return menu_controller.create_item(data, db)

@router.get("/menu-items/{id}")
def get_item(id: int, db: Session= Depends(get_db), user = Depends(get_current_user)):
    return menu_controller.get_item(id, db)

@router.put("/menu-items/{id}")
def update_item(id: int, data: MenuItemUpdate, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return menu_controller.update_item(id, data, db)


@router.delete("/menu-items/{id}")
def delete_item(id: int, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return menu_controller.delete_item(id, db)


# @router.get("/menu-items/category/{id}")
# def get_items_by_category(id: int, db: Session = Depends(get_db), user = Depends(get_current_user)):
#     return menu_controller.get_items_by_category(id, db)


# @router.get("/menu-items/available")
# def get_available_items(db: Session = Depends(get_db), user = Depends(get_current_user)):
#     return menu_controller.get_available_items(db)


# @router.get("/menu-items/category/{id}/available")
# def get_available_items_by_category(id: int, db: Session = Depends(get_db), user = Depends(get_current_user)):
#     return menu_controller.get_available_items_by_category(id, db)

